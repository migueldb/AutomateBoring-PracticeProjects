#! python3
# regexSearch.py - opens all .txt files in a folder and searches for any line
#                  that matches a user-supplied regular expression.

import os
import re

def regexSearch(extension, folderPath, searchString):
  for entry in os.scandir(folderPath):
    if entry.name.endswith(extension) and entry.is_file():
      testFile = open(os.path.join(folderPath, entry.name))
      testString = testFile.read()
      testFile.close()
      searchStringRegex = re.compile(searchString)
      if searchStringRegex.search(testString) == None:
        print('String "', searchString, '" not found in file', entry.name)
      else:
        print('String "', searchString, '" found in file', entry.name)


myExtension = '.txt'
myFolderPath = os.getcwd()
print('Enter your string:')
myString = input()

regexSearch(myExtension, myFolderPath, myString)
