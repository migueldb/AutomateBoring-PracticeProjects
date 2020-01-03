#! python3
# Automate Boring Stuff Practice Project - Chapter 4
# characterPictureGrid.py - Transposes a 2-dimensional list.

def transposeList(inputList):
  for i in range (len(inputList[0])):     # There is 6 items insided the first 
                                          # list of _grid_
    for j in range (len(inputList)):      # There is 9 lists inside variable 
                                          # _grid_
      print(inputList[j][i], end='')
    print('')

grid = [['.', '.', '.', '.', '.', '.',],
        ['.', '0', '0', '.', '.', '.',],
        ['0', '0', '0', '0', '.', '.',],
        ['0', '0', '0', '0', '0', '.',],
        ['.', '0', '0', '0', '0', '0',],
        ['0', '0', '0', '0', '0', '.',],
        ['0', '0', '0', '0', '.', '.',],
        ['.', '0', '0', '.', '.', '.',],
        ['.', '.', '.', '.', '.', '.',]]

transposeList(grid)
