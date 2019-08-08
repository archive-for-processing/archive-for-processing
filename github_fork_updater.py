#!/usr/bin/env python3

"""GitHub fork updater.

Usage:
configure credentials, then run
    github_fork_updater.py

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
that both the script and the shell have password access to the git account.

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

"""

from github import Github
import os
import config.config as cfg

def API_print_cache():
    """Display the API summary without needing to request it."""
    # print(dir(repos[0]))
    api_repo = ['CHECK_AFTER_INIT_FLAG', '_CompletableGithubObject__complete', '_CompletableGithubObject__completed', '_GithubObject__makeSimpleAttribute', '_GithubObject__makeSimpleListAttribute', '_GithubObject__makeTransformedAttribute', '_Repository__create_pull', '_Repository__create_pull_1', '_Repository__create_pull_2', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allow_merge_commit', '_allow_rebase_merge', '_allow_squash_merge', '_archive_url', '_archived', '_assignees_url', '_blobs_url', '_branches_url', '_clone_url', '_collaborators_url', '_comments_url', '_commits_url', '_compare_url', '_completeIfNeeded', '_completeIfNotSet', '_contents_url', '_contributors_url', '_created_at', '_default_branch', '_description', '_downloads_url', '_events_url', '_fork', '_forks', '_forks_count', '_forks_url', '_full_name', '_git_commits_url', '_git_refs_url', '_git_tags_url', '_git_url', '_has_downloads', '_has_issues', '_has_projects', '_has_wiki', '_headers', '_homepage', '_hooks_url', '_html_url', '_hub', '_id', '_identity', '_initAttributes', '_issue_comment_url', '_issue_events_url', '_issues_url', '_keys_url', '_labels_url', '_language', '_languages_url', '_makeBoolAttribute', '_makeClassAttribute', '_makeDatetimeAttribute', '_makeDictAttribute', '_makeDictOfStringsToClassesAttribute', '_makeIntAttribute', '_makeListOfClassesAttribute', '_makeListOfDictsAttribute', '_makeListOfIntsAttribute', '_makeListOfListOfStringsAttribute', '_makeListOfStringsAttribute', '_makeStringAttribute', '_makeTimestampAttribute', '_master_branch', '_merges_url', '_milestones_url', '_mirror_url', '_name', '_network_count', '_notifications_url', '_open_issues', '_open_issues_count', '_organization', '_owner', '_parent', '_parentUrl', '_permissions', '_private', '_pulls_url', '_pushed_at', '_rawData', '_requester', '_size', '_source', '_ssh_url', '_stargazers_count', '_stargazers_url', '_statuses_url', '_storeAndUseAttributes', '_subscribers_count', '_subscribers_url', '_subscription_url', '_svn_url', '_tags_url', '_teams_url', '_topics', '_trees_url', '_updated_at', '_url', '_useAttributes', '_watchers', '_watchers_count', 'add_to_collaborators', 'allow_merge_commit', 'allow_rebase_merge', 'allow_squash_merge', 'archive_url', 'archived', 'assignees_url', 'blobs_url', 'branches_url', 'clone_url', 'collaborators_url', 'comments_url', 'commits_url', 'compare', 'compare_url', 'contents_url', 'contributors_url', 'create_file', 'create_git_blob', 'create_git_commit', 'create_git_ref', 'create_git_release', 'create_git_tag', 'create_git_tag_and_release', 'create_git_tree', 'create_hook', 'create_issue', 'create_key', 'create_label', 'create_milestone', 'create_project', 'create_pull', 'create_source_import', 'created_at', 'default_branch', 'delete', 'delete_file', 'description', 'downloads_url', 'edit', 'etag', 'events_url', 'fork', 'forks', 'forks_count', 'forks_url', 'full_name', 'get__repr__', 'get_archive_link', 'get_assignees', 'get_branch', 'get_branches', 'get_clones_traffic', 'get_collaborator_permission', 'get_collaborators', 'get_comment', 'get_comments', 'get_commit', 'get_commits', 'get_contents', 'get_contributors', 'get_dir_contents', 'get_download', 'get_downloads', 'get_events', 'get_file_contents', 'get_forks', 'get_git_blob', 'get_git_commit', 'get_git_ref', 'get_git_refs', 'get_git_tag', 'get_git_tree', 'get_hook', 'get_hooks', 'get_issue', 'get_issues', 'get_issues_comments', 'get_issues_event', 'get_issues_events', 'get_key', 'get_keys', 'get_label', 'get_labels', 'get_languages', 'get_latest_release', 'get_license', 'get_milestone', 'get_milestones', 'get_network_events', 'get_projects', 'get_pull', 'get_pulls', 'get_pulls_comments', 'get_pulls_review_comments', 'get_readme', 'get_release', 'get_release_asset', 'get_releases', 'get_source_import', 'get_stargazers', 'get_stargazers_with_dates', 'get_stats_code_frequency', 'get_stats_commit_activity', 'get_stats_contributors', 'get_stats_participation', 'get_stats_punch_card', 'get_subscribers', 'get_tags', 'get_teams', 'get_top_paths', 'get_top_referrers', 'get_topics', 'get_views_traffic', 'get_watchers', 'git_commits_url', 'git_refs_url', 'git_tags_url', 'git_url', 'has_downloads', 'has_in_assignees', 'has_in_collaborators', 'has_issues', 'has_projects', 'has_wiki', 'homepage', 'hooks_url', 'html_url', 'id', 'issue_comment_url', 'issue_events_url', 'issues_url', 'keys_url', 'labels_url', 'language', 'languages_url', 'last_modified', 'legacy_search_issues', 'mark_notifications_as_read', 'master_branch', 'merge', 'merges_url', 'milestones_url', 'mirror_url', 'name', 'network_count', 'notifications_url', 'open_issues', 'open_issues_count', 'organization', 'owner', 'parent', 'permissions', 'private', 'pulls_url', 'pushed_at', 'raw_data', 'raw_headers', 'remove_from_collaborators', 'replace_topics', 'setCheckAfterInitFlag', 'size', 'source', 'ssh_url', 'stargazers_count', 'stargazers_url', 'statuses_url', 'subscribe_to_hub', 'subscribers_count', 'subscribers_url', 'subscription_url', 'svn_url', 'tags_url', 'teams_url', 'topics', 'trees_url', 'unsubscribe_from_hub', 'update', 'update_file', 'updated_at', 'url', 'watchers', 'watchers_count']
    # print(dir(repos[0].get_branch('master')))
    api_branch = ['CHECK_AFTER_INIT_FLAG', '_GithubObject__makeSimpleAttribute', '_GithubObject__makeSimpleListAttribute', '_GithubObject__makeTransformedAttribute', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_commit', '_completeIfNeeded', '_headers', '_initAttributes', '_makeBoolAttribute', '_makeClassAttribute', '_makeDatetimeAttribute', '_makeDictAttribute', '_makeDictOfStringsToClassesAttribute', '_makeIntAttribute', '_makeListOfClassesAttribute', '_makeListOfDictsAttribute', '_makeListOfIntsAttribute', '_makeListOfListOfStringsAttribute', '_makeListOfStringsAttribute', '_makeStringAttribute', '_makeTimestampAttribute', '_name', '_parentUrl', '_protected', '_protection_url', '_rawData', '_requester', '_storeAndUseAttributes', '_useAttributes', 'add_required_signatures', 'commit', 'edit_protection', 'edit_required_pull_request_reviews', 'edit_required_status_checks', 'edit_team_push_restrictions', 'edit_user_push_restrictions', 'etag', 'get__repr__', 'get_admin_enforcement', 'get_protection', 'get_required_pull_request_reviews', 'get_required_signatures', 'get_required_status_checks', 'get_team_push_restrictions', 'get_user_push_restrictions', 'last_modified', 'name', 'protected', 'protection_url', 'raw_data', 'raw_headers', 'remove_admin_enforcement', 'remove_protection', 'remove_push_restrictions', 'remove_required_pull_request_reviews', 'remove_required_signatures', 'remove_required_status_checks', 'setCheckAfterInitFlag', 'set_admin_enforcement']
    # print(dir(repos[0].get_branch('master').commit))
    api_commit = ['CHECK_AFTER_INIT_FLAG', '_CompletableGithubObject__complete', '_CompletableGithubObject__completed', '_GithubObject__makeSimpleAttribute', '_GithubObject__makeSimpleListAttribute', '_GithubObject__makeTransformedAttribute', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_author', '_comments_url', '_commit', '_committer', '_completeIfNeeded', '_completeIfNotSet', '_files', '_headers', '_html_url', '_identity', '_initAttributes', '_makeBoolAttribute', '_makeClassAttribute', '_makeDatetimeAttribute', '_makeDictAttribute', '_makeDictOfStringsToClassesAttribute', '_makeIntAttribute', '_makeListOfClassesAttribute', '_makeListOfDictsAttribute', '_makeListOfIntsAttribute', '_makeListOfListOfStringsAttribute', '_makeListOfStringsAttribute', '_makeStringAttribute', '_makeTimestampAttribute', '_parentUrl', '_parents', '_rawData', '_requester', '_sha', '_stats', '_storeAndUseAttributes', '_url', '_useAttributes', 'author', 'comments_url', 'commit', 'committer', 'create_comment', 'create_status', 'etag', 'files', 'get__repr__', 'get_combined_status', 'get_comments', 'get_statuses', 'html_url', 'last_modified', 'parents', 'raw_data', 'raw_headers', 'setCheckAfterInitFlag', 'sha', 'stats', 'update', 'url']
    print('api_repo:\n', api_repo, '\n')
    print('api_branch:\n', api_branch, '\n')
    print('api_commit:\n', api_commit, '\n')

def main(user, passwd, orgname):
    g = Github(user, passwd)
    # g = Github("access_token")

    repos = g.get_organization(orgname).get_repos()

    unpack_root = '/Users/jeremydouglass/git/__unpack_archive'
    os.makedirs(unpack_root, exist_ok=True)

    # for repo in g.get_user().get_repos():

    print('Checking each forked repo for a source whose master branch' +
          'has a more recent commit')
    for repo in repos:
        print('...', repo.name)
        try:
            load_orig_clone_url = repo.source.clone_url
        except (AttributeError) as err:
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
    username=''
    password=''
    org_name=''
    if username and password and org_name:
        main(username, password, org_name)
    else:
        main(cfg.MY_USERNAME, cfg.MY_PASSWORD, cfg.MY_GITHUB_ORG)
