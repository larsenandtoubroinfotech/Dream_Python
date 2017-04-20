#!/usr/bin/python
import sys
textToReplace = sys.argv[1]
textToSearch = sys.argv[2]
file_name = sys.argv[3]
filedata = None
with open(file_name, 'r') as file :
  filedata = file.read()
filedata = filedata.replace(textToSearch, textToReplace)
with open(file_name, 'w') as file:
  file.write(filedata)
