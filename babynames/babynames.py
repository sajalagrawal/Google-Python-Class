# Author- SAJAL AGRAWAL
# sajal.agrawal1997@gmail.com

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def _count():
    i = 0
    while 1:
        yield i
        i += 1
      
def sorted(iterable, key=None, reverse=False):
    'Drop-in replacement for the sorted() built-in function (excluding cmp())'
    'if using python 2 instead of python 3'
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
  
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # The list [year, name_and_rank, name_and_rank, ...] we'll eventually return.
  names=[]
  
  # Open and read the file.
  f=open(filename,'rU')
  text=f.read()
  
  #get the year
  year=re.search(r'Popularity\sin\s(\d\d\d\d)',text)
  if not year:
    sys.stderr.write('Year couldn\'t be found.')
    sys.exit(1)

  names.append(year.group(1))

  # Extract all the data tuples with a findall()
  # each tuple is: (rank, boy-name, girl-name)
  #<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
  tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',text)

  # Store data into a dict using each name as a key and that
  # name's rank number as the value.
  # (if the name is already in there, don't add it, since
  # this new rank will be bigger than the previous rank).
  namesToRank={}
  for rankTuple in tuples:
    (rank,boyname,girlname)=rankTuple    # unpack the tuple into 3 vars
    if(boyname not in namesToRank): 
      namesToRank[boyname]=rank
    if(girlname not in namesToRank):
      namesToRank[girlname]=rank

  # Get the names, sorted in the right order      
  sortedNames=sorted(namesToRank.keys())

  for name in sortedNames:
    names.append(name+ " " +namesToRank[name] )
  
  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names=extract_names(filename)

  text='\n'.join(names)

  if summary:
    outf=open(filename+'.summary','w')
    outf.write(text)
    outf.close()
  else:
    print text
  
  
if __name__ == '__main__':
  main()
