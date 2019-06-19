#!/usr/bin/env python3

# Download listing txt and zip build artifacts for all 
# Contributions Manager listings:
#   Libraries, Examples, Tools, and Modes
# -- including disabled, if available --

import logging
import os
import re
import urllib.request
import urllib.parse

basepath = os.path.join(os.getcwd(), 'contributions')

def save_urlfile(result, path):
    os.makedirs(path, exist_ok=True)
    a = urllib.parse.urlparse(result)
    aname = os.path.basename(a.path)
    fullfilename = os.path.join(path, aname)
    print(fullfilename)
    if not os.path.exists(aname):
        try:
            urllib.request.urlretrieve(result, fullfilename)
            logging.info('...saved: %s', result)
        except (urllib.error.HTTPError, urllib.error.URLError) as err:
            logging.warning('%s:%s', err, result)
    else:
        logging.info('...exists: %s', aname )

# start logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(basepath, 'contrib_archive')),
        logging.StreamHandler()
    ])

# source listing
url = 'https://raw.githubusercontent.com/processing/processing-docs/master/contrib_generate/sources.conf'

# get full listing -- entry format is
#   017 \ http://mrfeinberg.com/peasycam/peasycam.txt
f = urllib.request.urlopen(url)
f_text = f.read().decode('utf-8')
with open(os.path.join(basepath, 'sources.conf'), 'w') as f:
    logging.info('Saving sources')
    f.write(f_text)

# # parsing as a config file works, but it skips commented-out lines,
# # so it cant discover or log disabled resources
# import configparser
# config = configparser.ConfigParser(allow_no_value=True, delimiters=['\\'])
# config.read_string(f_text)
# for each_section in config.sections():
#     for (each_key, each_val) in config.items(each_section, raw=True):
#         print(each_section, each_key, each_val)

# instead parse for txt urls -- this will also find disabled entries like
#   #404# 117 \ http://ccl.angusforbes.com/stereo.txt
p = re.compile('http.*\.txt')
results = p.findall(f_text)

# loop over urls
for url_txt in results:
    # ownload txt, if not downloaded
    txt_output_dir = os.path.join(basepath, 'txt')
    save_urlfile(url_txt, txt_output_dir)
    # build artifact by convention is .zip corresponding to .txt
    # ownload zip, if not downloaded
    url_zip = re.sub('.txt$', '.zip', url_txt)
    zip_output_dir = os.path.join(basepath, 'zip')
    save_urlfile(url_zip, zip_output_dir)
