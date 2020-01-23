#! python3
# Automate Boring Stuff Practice Project - Chapter 17
# findPhotoFolders.py - Finds photo folders and returns their absolute path
#
# NOTE: This module uses Pillow module for images handling.  Please refer to:
#       https://pypi.org/project/Pillow/
#       for more information 

# This fuction checks a file _fileName_ agains a list of extensions
# _extensionsList_.
def validateExtensions(_fileName_, _extensionsList_):
  # Loop through every extension in _extensionList_
  valid = False
  for extension in _extensionsList_:
    # The valid binary variable is kept True if at least one of the extensions
    # matches the file extension
    if  _fileName_.lower().endswith(extension):
      valid = True 
      continue
  return valid

import os
from PIL import Image

# Get the search path (OS independent - current drive's root)
searchPath = os.path.abspath(os.sep)
# list of image file extensions.  User can add / remove as required.
extensionsList = ['.png', '.jpg', '.gif', '.bmp', '.jpeg']
# Minimum size criteria
searchCriterium = 500

# Walk all folders subfolders
for foldername, subfolders, filenames in  os.walk(searchPath):
  # Photo files counters
  numPhotoFiles = 0
  numNonPhotoFiles = 0
  # Loop through file names in current folder
  for filename in filenames:
    # Check if the file has a photo extension by calling the function
    # validateExtensions
    if not validateExtensions(filename, extensionsList):
      numNonPhotoFiles += 1
      continue
    
    # Open image file using Pillow.  If error increase non-photos counter
    try:
      im = Image.open(os.path.join(foldername, filename))
      # Get image dimensions
      width, height = im.size
    except IOError:
      numNonPhotoFiles += 1
      continue

    # Check if width & heigth are larger than search criterium    #print('Checking file %s' % os.path.join(searchPath, foldername, filename))
    if width >= searchCriterium and height >= searchCriterium:
      # Image is large enough to be considered a photo.
      numPhotoFiles += 1
    else:
      # Image is too small to be a photo.
      numNonPhotoFiles += 1
  
  # If more than half of files where photos,
  # print the absolute path of the folder
  if numNonPhotoFiles < numPhotoFiles:
    print("Here's a probable photo folder: %s" % os.path.abspath(foldername))
