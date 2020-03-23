#!/usr/bin/env bash

# MY NOTES ON UPDATING

# 1. merge master into data
# 2. then run this scriipt to  download updated txt and zip
workon archive_for_processing
./contributions/contrib_archive.py
# 3. after, commit txt to data branch
# 4. then merge data into zip branch
# 5. then commit zip to zip

# independently, update forks
# this is a separate local dir,
# shouldn't affect repo files
cd forks
./github_fork_updater.py 
