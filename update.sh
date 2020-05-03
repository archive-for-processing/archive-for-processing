#!/usr/bin/env bash

# MY NOTES ON UPDATING

dateslug=$(date '+%Y%m%d') # YYMMDD
txtcommit="contributions/txt: update $dateslug"
zipcommit="contributions/zip: update $dateslug"

# 0. switch to correect virtualenv for python
#    with github api requirements installed
#    as per setup
source ~/.bash_profile
workon archive_for_processing

# independently, update forks
# this is a separate local dir,
# shouldn't affect repo files
# ...first apply credentials from stash
git stash apply stash@{0}
read -n1 -r -s -p "Updating forks: Press any key to continue or Ctrl-C to exit..."
cd forks
./github_fork_updater.py 
cd ../
# remove credentials
git checkout -- config/config.py
# exit virtualenv workon
deactivate

# 1. merge master into data
git checkout data
git merge master --log --no-edit

# 2. download updated txt and zip
./contributions/contrib_archive.py

# 3. commit txt to data
git add contributions/sources.conf
git add contributions/txt/\*.txt
git status
printf "\n$txtcommit\n"
read -n1 -r -s -p "Press any key to continue or Ctrl-C to exit..."
git commit -m "$txtcommit"

# 4. cachee zips
#    ...because our zips are ignored on our main branch
#     we will need to copy them over so that git doesn't
#     wipe them out.
tmp_dir=$(mktemp -d -t tmp)
mv contributions/zip/*.zip $tmp_dir/

# 5. copy data into zip branch
git checkout ZIP_DATA_NOPUSH
git merge data --log --no-edit

# 6. add zips to zip branch and commit
mv $tmp_dir/*.zip contributions/zip/
git add contributions/zip/\*.zip
git status
printf "\n$zipcommit\n"
read -n1 -r -s -p "Press any key to continue or Ctrl-C to exit..."
git commit -m "$zipcommit"

# return to default branch
git checkout master
printf "\nDone!\n\n"
