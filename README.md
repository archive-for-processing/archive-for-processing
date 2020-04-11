# Archive for Processing

Archive for Processing is an (unofficial) archive of resources for the Processing community. It collects software related to Processing, p5.js, Python mode / Processing.py, p5py, pyp5js, R Mode / Processing.R, and other related languages, modes, libraries, and tools.

It is intended to make the distributed ecosystem of open source libraries, modes, tools, example sets, and documentation a bit more robust. It does this by acting as a fallback, providing simple redundancy via a list of forked GitHub repositories and offline backup for distributed binaries. These forks and binary backups are to help guard against future project loss. In particular, given that many of the core open source resources of the Processing community are generously self-hosted by their contributing authors, the archive attempt to keep such works available even if their associated accounts, websites, et cetera are no longer maintained.

Archive for Processing may also serve as a list / index for browsing the amazing variety of Processing resources. However, this is an infrequently updated archive, not a directory -- it is not comprehensive. More importantly, it is **not a live mirror**! Always use original official author repositories whenever available.

This GitHub organization account approaches this goal in the following ways:

1. Forks:
   -  Maintain a list of forks of public GitHub repositories.
   -  The forks are browseable from the github organization page:
      https://github.com/archive-for-processing
   -  For projects under development or maintainence, the forks
      are periodically updated to their latest master commit.
   -  To recommend a fork, open an issue on this repo.

2. Contributions
   -  Libraries, Tools, and Modes disseminated through the PDE
      Contributions Manager periodically have their metadata
      with pointers to the latest properties files and download URLs
      backed up to the /data branch of this repo.
   -  Binaries are periodically backed up offline. These files
      are not distributed through GitHub, but are archived in case
      an old release is lost.

This archive contains both inactive and active projects -- it includes forks of ongoing, under-development repositories. When viewing a repository in the archive, **FIRST CHECK THE SOURCE REPO** linked under the title, if that original source exists. The archival forks may be out-of-date, with an up-to-date version being developed by the original author or maintainer. Forks for active repositories do not automatically update -- they are snapshots that must be periodically refreshed.

Like the work of the Processing Foundation, which is developed and distributed through GitHub, Archive for Processing collections are biased towards collecting GitHub-based projects. There are software tools in the Processing ecosystem that were set up to be distributed in other ways -- either via another public repo such as Google Code, SourceForge, BitBucket, et cetera, or self-hosted. Identifying and developing a workflow to archive those resources is an ongoing effort.

The repository forks here are not maintained in any way, even if the original is no longer available. As such, they do not accept issues, comments, etc. They are available to fork for interested developers, including future volunteer maintainers.

This independent initiative is not an official project of the Processing Foundation.

## Scripts

This repository contains two main scripts:

1.  contributions/contrib_archive.py

    Downloads all PDE Contributions Manager listings: Libraries, Examples,
    Tools, and Modes -- including disabled, if available -- as txt listings
    and zip files.
    
    -  txt listings are archived in the 'data' branch, under contributions/txt
    -  zip files are not stored in this repository

2.  github_fork_updater.py

    Attempts to periodically keep the master branch of all forks on all repos
    up-to-date on GitHub, using the API and the following sequence:
    
    ```
    git clone repo_url
    git remote add upstream repo.source.clone_url
    git fetch upstream
    git checkout master
    git merge upstream/master
    git push
    ```

## Sources

The GitHub project account contains a large number of forked repos.
These are maintained through a github org account and its forks.
Some of these (and some resources which are not repos, or cannot be forked) are found below in a manually updated and sorted list. Repo forks are periodically brought up to date on their master branch with `github_fork_updater.py` 

Forks are only made of public repos. If accounts are removed, repos are deleted, or repos are taken private, the archive fork attempts to preserve that last public snapshot of the repo.

> https://help.github.com/en/articles/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility
>
> **Deleting a public repository**  
> When you delete a public repository, one of the existing public forks is chosen to be the new parent repository. All other repositories are forked off of this new parent and subsequent pull requests go to this new parent.
> 
> **Changing a public repository to a private repository**  
> If a public repository is made private, its public forks are split off into a new network. As with deleting a public repository, one of the existing public forks is chosen to be the new parent repository and all other repositories are forked off of this new parent. Subsequent pull requests go to this new parent.

### Libraries forked from the Library Template

A key limitation is that the Processing Library Template has been forked by a number of projects.
Each of these projects counts as the "same repo," and thus only one of all of them can be forked by the Archive for Processing account.

A workaround might involve iterating over an "unforkable" url list and treating as a remote for a clean repo outside the API.

## Collecting

For further information on specific repos or categories of repos, see [COLLECTING.md]().
