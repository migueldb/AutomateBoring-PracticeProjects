#! python3
# Automate Boring Stuff Practice Project - Chapter 9
# insertingGaps.py -  finds all files with a given prefix, such as
# spam001.txt, spam002.txt, spam003.txt and inserts gaps into numbered files so
# that a new file can be added.

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

def insertGap(filesList, figures, prefix, folder, gapPosition):
  for i in range(len(filesList),gapPosition-1,-1):
    # print(i)
    shutil.move(os.path.join(folder,filesList[i-1]), os.path.join(folder, \
                prefix + (figures-len(str(i))) * '0' + str(i+1) + '.txt'))
    # print(os.path.join(folder,filesList[i-1]))

# User is required to input the following variables

myPrefix = 'spam'
myFigures = 3
myPattern = r'^(' + myPrefix + r')(\d){' + str(myFigures) + '}'
myFolder = os.getcwd()
myGapPosition = 2


myList = createFileList(myPattern, myFolder)
# print('Files matching: '+ str(myList))
# print(len(myList))
insertGap(myList, myFigures, myPrefix, myFolder, myGapPosition)
