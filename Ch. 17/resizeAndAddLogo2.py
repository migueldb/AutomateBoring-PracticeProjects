#! python3
# Automate Boring Stuff Practice Project - Chapter 17
# resizeAndAddLogo2.py - Improved version of the ResizeAndAddLogo.py
#
# NOTE: The original file, the logo, and the required images can be found at the
#       link location below:
#       https://nostarch.com/download/
#       Automate_the_Boring_Stuff_onlinematerials_v.2.zip
#       This module uses Pillow module for images handling.  Please refer to:
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

# This function calculates the logo resize factor
def calculateLogoRF(_imageWidth_, _imageHeight_, _logoWidth_, _logoHeight_, \
                      _factor_):
  # Calculate width/height ratio for image and logo
  imageSizeRatio = _imageWidth_ / _imageHeight_
  logoSizeRatio = _logoWidth_ / _logoHeight_
  # If the logo width/height ratio is larger than image's
  if logoSizeRatio >= imageSizeRatio:
    # Calculate the resize factor so the logo's width is _factor_ times smaller
    # than the image
    logoResizeFactor = (_logoWidth_ * _factor_) / _imageWidth_
  else:
    # if the logo width/height ratio is lower than image's
    # Calculate the resize factor so the logo's height is _factor_ times smaller
    # than the image
    logoResizeFactor = (_logoHeight_ * _factor_) / _imageHeight_
  # Return factor
  return logoResizeFactor

import os
from PIL import Image
# The images will be resized to fit a 300x300 square logo
SQUARE_FIT_SIZE = 300
# The logo file name
LOGO_FILENAME = 'catlogo.png'

# This is how many times bigger than the logo the image is required to be
factor = 2
# List of image file extensions, the user can add or remove as required
extensionsList = ['.png', '.jpg', '.gif', '.bmp']
# Create a directory to store the images with logo
os.makedirs('withLogo', exist_ok =True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
  # skip non-image files and the logo file itself
  if not validateExtensions(filename, extensionsList) \
  or filename == LOGO_FILENAME:
    continue
  
  # Open logo
  logoIm = Image.open(LOGO_FILENAME)
  # Get logo dimensions and print a message
  logoWidth, logoHeight = logoIm.size
  print('Current logo size is: %sx%s' % (logoWidth, logoHeight))

  # Open image file
  im = Image.open(filename)
  # Get logo dimensions and print a message
  width, height = im.size
  print('Current image size is: %sx%s' % (width, height))

  # Check if the image needs to be resized.
  if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
    # Calculate the new width and height to resize to.
    if width > height:
      height = int((SQUARE_FIT_SIZE / width) * height)
      width = SQUARE_FIT_SIZE
    else:
      width = int((SQUARE_FIT_SIZE / height) * width)
      height = SQUARE_FIT_SIZE
    
    # Resize the image.
    print('Resizing %s...' % filename)
    im = im.resize((width, height))

  # Get the image resize factor by calling the function calculateLogoRF
  LOGO_RESIZE_FACTOR = calculateLogoRF(width, height, logoWidth, logoHeight, \
                      factor)
  # Print a message with the logo resize factor
  print('Logo resize factor: %s' % LOGO_RESIZE_FACTOR)
  # Resize logo
  logoIm = logoIm.resize((int(logoWidth / LOGO_RESIZE_FACTOR), \
                          int(logoHeight / LOGO_RESIZE_FACTOR)))

  # Get new logo dimensions and update variables
  logoWidth, logoHeight = logoIm.size

  # Print new logo dimensions
  print('New logo size %sx%s' % (logoHeight, logoWidth))

  # Add the logo to the image
  print('Adding the logo to %s' % filename)
  im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
 
  # Save changes.
  logoIm.close()
  im.save(os.path.join('withLogo', filename))
