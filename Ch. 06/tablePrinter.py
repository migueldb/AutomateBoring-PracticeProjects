#! python3
# Automate Boring Stuff Practice Project - Chapter 6
# tablePrinter.py - displays a well-organized table from a list of lists of strings

def findLongestString(inputList):
  colWidth = 0
  for i in range(len(inputList)):
    for j in range(len(inputList[0])):
      if len(inputList[i][j]) > colWidth:
        colWidth = len(inputList[i][j])
  return colWidth

def printTable(inputList, stringLength):
  for i in range (len(inputList[0])):
    for j in range (len(inputList)):
      print(inputList[j][i].rjust(stringLength) ,end='')
    print('')



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# findLongestString(tableData)
printTable(tableData, findLongestString(tableData))
