#! python3
# Automate Boring Stuff Practice Project - Chapter 9
# selectiveCopy.py - walks through a folder tree and searches for files with a
# certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder

import shutil, os

def selCopy(folderTree, extension, newFolder):

  folderTree =  os.path.abspath(folderTree)   # make sure folder is absolute
  newFolder = os.path.abspath(newFolder)      # make sure folder is absolute
  if not os.path.isdir(newFolder):
    os.mkdir(newFolder)                       # make sure newFolder exist as 
                                              # a folder

  os.chdir(folderTree)

  for foldername, subfolders, filenames in os.walk(folderTree):
    if foldername == newFolder:               # skip newFolder
      continue
    print('Analizing contents of %s folder...' % (foldername))
    for filename in filenames:
      if not filename.endswith(extension):
        continue
      print('File %s found.  Copying it to %s...' % (os.path.join(foldername, filename), newFolder))
      shutil.copy(os.path.join(foldername, filename), newFolder)

# User is required to input the following variables

myFolderTree = 'C:\\my\\disk\\location\\'
myExtension = '.py'
myNewFolder = os.path.join(myFolderTree, 'myNewLocation')

selCopy(myFolderTree, myExtension, myNewFolder)
