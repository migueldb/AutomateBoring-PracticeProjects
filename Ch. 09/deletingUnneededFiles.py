#! python3
# Automate Boring Stuff Practice Project - Chapter 9
# deletingUnneededFiles.py - walks through a folder tree and searches for
# exceptionally large files or folders—say, ones that have a file size of more
# than 100MB and prints these files with their absolute path to the screen.

import os

def findLargeFilesOrFolders(folderTree, maxSizeMB):

  folderTree =  os.path.abspath(folderTree)   # make sure folder is absolute

  for foldername, subfolders, filenames in os.walk(folderTree):
    for subfolder in subfolders:
      #print('Analizing contents of %s subfolder...' % (os.path.join(foldername, subfolder)))
      subfolderSizeMB = 0.0
      for subfoldername, subsubfolders, subfilenames in os.walk(os.path.join(foldername, subfolder)):
          for subfilename in subfilenames:
            subfilenameSize = os.path.getsize(os.path.join(subfoldername, subfilename))/(1024**2)
            if not subfilenameSize >= maxSizeMB:
              continue
            print('File %s size is %s MB' % (os.path.join(subfoldername, subfilename),subfilenameSize))
            subfolderSizeMB += subfilenameSize
      #print('Subfolder %s size is %s MB' % (subfolder, subfolderSizeMB) )
      if not subfolderSizeMB >= maxSizeMB:
        continue
      print('Subfolder %s size is %s MB' % (subfolder, subfolderSizeMB))

# User is required to input the following variables

myFolderTree = 'C:\\my\\disk\\location\\'
myMaxSizeMB = 100.0

findLargeFilesOrFolders(myFolderTree, myMaxSizeMB)
