#!/usr/bin/python
import sys
textToReplace = sys.argv[1]
textToSearch = sys.argv[2]
file_name = sys.argv[3]
filedata = None
with open(file_name, 'r') as f:
    filedata = f.read()
filedata = filedata.replace(textToSearch, textToReplace)
with open(file_name, 'w') as f:
    f.write(filedata)
