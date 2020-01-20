#! python3
# Automate Boring Stuff Practice Project - Chapter 9
# fillingInTheGaps.py -  finds all files with a given prefix, such as
# spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps
# in the numbering (such as if there is a spam001.txt and spam003.txt but no
# spam002.txt). Then renames all the files to close the gap.
# The function createFileList() generates the required files with gaps in
# preparation.

import os, re, shutil

def createFileList(namePattern, folder):
  fileNameRegex = re.compile(namePattern)
  myCounter = 0
  filesList = []
  for filename in os.listdir(folder):
    if fileNameRegex.search(filename) == None:
      continue
    #myCounter += 1
    filesList += [filename]
  filesList.sort()
  return filesList



def fillTheGaps(gappyList, figures, prefix, folder):
  for i in range(len(gappyList)):
    if gappyList[i] == prefix + (figures-len(str(i+1))) * '0' + str(i+1):
      continue
    shutil.move(os.path.join(folder,gappyList[i]), os.path.join(folder, \
                prefix + (figures-len(str(i+1))) * '0' + str(i+1) + '.txt'))  

def createNumFiles(prefix, folder, figures):
  for filename in os.listdir(folder):
    if filename.endswith('.txt'):   # clean folder from previous .txt files
      os.unlink(filename)

  for i in range(3):
    testFile = open(os.path.join(folder, myPrefix + (myFigures-1) * '0' + \
                                 str(1+2*i) + '.txt'), 'w')
    testFile.close()

# User is required to input the following variables
 
myPrefix = 'spam'
myFigures = 3
myPattern = r'^(' + myPrefix + r')(\d){' + str(myFigures) + '}'
myFolder = os.getcwd()

createNumFiles(myPrefix, myFolder, myFigures)
myList = createFileList(myPattern, myFolder)
print('Files matching: '+ str(myList))
print(len(myList))
fillTheGaps(myList, myFigures, myPrefix, myFolder)
