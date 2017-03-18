# Author- SAJAL AGRAWAL
# sajal.agrawal1997@gmail.com

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


#to view the urls
#"logpuzzle.py ./animal_code.google.com" or "logpuzzle.py ./place_code.google.com"

#to download image slices and join them into a single picture
#"logpuzzle.py --todir dest ./animal_code.google.com" where dest is destination folder

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def _count():
    i = 0
    while 1:
        yield i
        i += 1

def sorted(iterable, key=None, reverse=False):
    'Drop-in replacement for the sorted() built-in function (excluding cmp())'
    seq = list(iterable)
    if reverse:
        seq.reverse()
    if key is not None:
        seq = zip(map(key, seq), _count(), seq)
    seq.sort()
    if key is not None:
        seq = map(lambda decorated: decorated[2], seq)
    if reverse:
        seq.reverse()
    return seq
  
def urlSortKey(url):
  """Used to order the urls in increasing order by 2nd word if present."""
  match=re.search(r'(\w+)-(\w+)\.\w+',url)
  if match:
    return match.group(2)
  else:
    return url

 
def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  underbar=filename.index('_')
  host=filename[underbar+1:]

  # Store the ulrs into a dict to screen out the duplicates at the end
  # will return only the keys(i.e. url) and not the values
  urlDict={}

  f=open(filename)

  for line in f:
    # Find the path which is after the GET and surrounded by spaces.
    match=re.search(r'GET\s(\S+)',line)
    if match:
      path=match.group(1)
      if 'puzzle' in path:
        urlDict['http://'+host+path]=1

  return sorted(urlDict.keys(),key=urlSortKey)
  
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  index=open(os.path.join(dest_dir, 'index.html'),'w')
  index.write('<html><body>\n')

  i=0
  for url in img_urls:
    localName='img'+str(i)
    print ('Retrieving...',url)
    urllib.urlretrieve(url,os.path.join(dest_dir,localName))

    index.write('<img src="%s">' % (localName,))
    i=i+1

  index.write('\n</body></html>')
  index.close()


def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])  #args[0] is apache logfile here eg: animal_code.google.com

  if todir:
    download_images(img_urls, todir)
  else:
    text='\n'.join(img_urls)
    print (text)

if __name__ == '__main__':
  main()
