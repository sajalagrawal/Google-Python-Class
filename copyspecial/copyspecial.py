#Author- SAJAL AGRAWAL
#sajal.agrawal1997@gmail.com

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

#"babynames.py ."
#this will list out the special files with their absolute paths present in the
#directories specified as arguments

#"babynames.py --todir dest ."
#this will make a folder named 'dest' if it doesn't already exists and copy
#all the special files to this folder.

#"babynames.py --tozip blah.zip ."
#this will make a zip file named 'blah.zip' and copy all
#the special files to this folder.

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dirname):
  """Given a dirname, returns a list of all its special files."""
  result=[]
  paths=os.listdir(dirname)
  for fname in paths:
    match=re.search(r'__(\w+)__',fname)
    if(match):
      result.append(os.path.abspath(os.path.join(dirname,fname)))      
  return result

def copy_to(paths,to_dir):
  """Copy all of the given files to the given dir, creating it if necessary."""
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname=os.path.basename(path)
    shutil.copy(path,os.path.join(os.path.abspath(to_dir),fname))

  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  
  # +++your code here+++
  # Call your functions

  paths=[]
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(paths,todir)
  else:
    ans='\n'.join(paths)
    print ans

    
if __name__ == "__main__":
  main()
