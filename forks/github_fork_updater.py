#!/usr/bin/env python3

"""GitHub fork updater.

Usage:
configure credentials, then run
    github_fork_updater.py

1. Uses GitHub API to retrieve a list of forks from an account
2. Checks the remote fork against its source for changed source.master commits
3. If the source changed, clones the fork, pulls the source, and pushes to fork
   (all on master) -- bringing that fork up-to-date on GitHub

Clones are downloaded to a cache directory. Depending on the total number of
forks to check, the total number of forks to be brought up-to-date, and whether
out-of-date forks are already locally cloned in the cache during a previous
script run, the total run time may range from minutes to hours. A run checking
~250 repositories and updating 5 of them took just under 10 minutes.

The cache is useful on repeat clones, as it saves bandwidth and time. However
it may be deleted any time the script is not running. On subsequent runs only
updated repos will be cloned -- so an initial cache of 250 sites may be
deleted and on a subsequent run will become a cache of 5 sites.


HOWEVER, there is one site in particular -- sketch-a-day -- that is 5GB, and
updated daily. If the cache is deleted, the whole 5GB must be downloaded again!


Background:

In order to keep all forks on all repos up-to-date on GitHub.
Ideally I would like to use the API to drop a fork and re-fork it, only if the
source still exists.

However, GitHub doesn't make this easy. There is an elaborate method through
the web UI. Otherwise, there is a recommended process to sync a fork as
described here https://help.github.com/en/articles/syncing-a-fork :

    ## add the original repository as remote repository called "upstream"
    git remote add upstream https://github.com/ORIGINAL_OWNER/REPOSITORY.git
    ## fetch all changes from the upstream repository
    git fetch upstream
    ## switch to the master branch of your fork
    git checkout master
    ## merge changes from the upstream repository into your fork
    git merge upstream/master
    ## push updated fork to github
    git push

The script currently uses PyGitHub to get the list of repos and their sources,
then uses os.system calls to execute with git on the command line. This assumes
that both the script and the shell have token access to the git account.

This could have been wrapped into a small shell command and called from python.
Other ways of doing the checkout / merge / push might include:

1. python subprocess
2. possibly pygithub facilities?
3. or using pygit2 to issue git commands

see https://stackoverflow.com/a/49458412/7207622
or https://pygithub.readthedocs.io/en/latest/examples/Commit.html

A limitation of this script is that it currently detects updates on master only,
and brings forks up to date on master only. Other branches are not tracked.
Ideally PyGitHub loops through the branches, checking each, and then updates the
branches detected as out of date using git. Not sure if that is possible. 

This script might be extended to build an index of forks.
It could also be adapted to run on top of a full backup -- this is currently
configured as backupless, with a cache directory that can be manually flushed,
but it never downloads everything from GitHub, only things that need to be
merged and pushed. There are other "full backup" tools for org accounts that
it could perhaps integrate with running on top of, rather than trying to
recreate. Then perhaps the wiki could be used rather than the README.txt for
indexing.

Notes:

Currently os.system('git clone') logs an error if a repo has previously been
added to the cache:

    fatal: destination path 'p5.ble.js' already exists and is not an empty
    directory.

However this error is fine; subsequent git commands work as long as the
original clone operation was successful / valid.

"""

from github import Github, GithubException
import os

import sys
sys.path.append('..')
import config.config as cfg

def main(token, orgname):
    g = Github(token)
    # g = Github("access_token")

    repos = g.get_organization(orgname).get_repos()

    unpack_root = os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'archive-for-processing--cache', 'repos'))
    os.makedirs(unpack_root, exist_ok=True)

    # for repo in g.get_user().get_repos():

    print('Checking each forked repo for a source whose master branch ' +
          'has a more recent commit')
    for repo in repos:
        print('...', repo.name)
        try:
            load_orig_clone_url = repo.source.clone_url
        except (AttributeError) as err:
            print(err)
            continue
            
        # some repos, eg p5jsShaderExamples, don't have a master branch at all
        try:
            msha = repo.get_branch('master').commit.sha
        except (GithubException) as err:
            print(err)
            continue
        
        if repo.clone_url and repo.source.clone_url and repo.get_branch('master').commit.sha != repo.source.get_branch('master').commit.sha:

            # Note that this doesn't always work.
            # for example, proscene shows its upstream clone from the template
            # and not the fact that archive forked from proscene
            # https://github.com/archive-for-processing/proscene.git
            # https://github.com/processing/processing-library-template.git
            # ... as a result, the last commit hashes don't match, even
            # though the archive fork is up to date with the proscene fork:
            # 88384b1322e107cf0774cf44ed65f00002a3d877
            # 92f571b09dd0cb20c1fd48412ce2d2027393ce6c
            # Temporary workaround -- skip forks of forks of the processing
            # template -- of which there should only be ONE due to github
            # technical limitations on forking.
            if repo.source.clone_url=='https://github.com/processing/processing-library-template.git':
                continue

            # One weird error -- commits don't match, but nothing to update.
            # As with the template, the issue appears to be that it is
            # a fork of a fork.
            #
            # ... p5.ble.js
            # https://github.com/archive-for-processing/p5.ble.js.git : https://github.com/yining1023/p5.ble.js.git
            # bb1f3b37c8b7666a2c87b505da772aa7c78e0588 : 09fc26e7e920594c87c7aac41104411978bf6e4c
            # fatal: destination path 'p5.ble.js' already exists and is not an empty directory.
            # unpack_dir: /Users/jeremydouglass/git/__unpack_archive/p5.ble.js
            # fatal: remote upstream already exists.
            # Already on 'master'
            # Your branch is up-to-date with 'origin/master'.
            # Already up-to-date.
            # Everything up-to-date

            print('repos:\n  ', repo.clone_url, '\n  ', repo.source.clone_url)
            print('commits:\n  ', repo.get_branch('master').commit.sha, '\n  ', repo.source.get_branch('master').commit.sha, '\n')

            # Note that repo.source.last_modified is always identical to
            # repo.last_modified even when the repo is out of date.

            os.chdir(unpack_root)
            print(os.system("git clone " + repo.clone_url))
            unpack_dir = os.path.join(unpack_root, repo.name)
            print('unpack_dir:', unpack_dir)
            os.chdir(unpack_dir)

            cmds = []
            cmds.append("git remote add upstream " + repo.source.clone_url)
            cmds.append("git fetch upstream")
            cmds.append("git checkout master")
            cmds.append("git merge upstream/master")
            cmds.append("git push")
            for cmd in cmds:
                print(os.system(cmd))

if __name__ == "__main__":
    # Either configure here or in config/config.py
    token=''
    org_name=''
    if token and org_name:
        main(token, org_name)
    else:
        main(cfg.MY_GITHUB_TOKEN, cfg.MY_GITHUB_ORG)
