#! python3
# Automate Boring Stuff Practice Project - Chapter 17
# customSeating.py - Creates custom seating cards from list
#
# NOTE: This script uses Pillow module for images handling.  Please refer to:
#       https://pypi.org/project/Pillow/
#       for more information
#       This script also requires a guest list in a txt file format. This
#       file can be downloaded here:
#       https://nostarch.com/download/
#       Automate_the_Boring_Stuff_onlinematerials_v.2.zip
#       A bacground image is required as well, the image name is stored in the
#       variable: backgroundImg

# This fuction creates the seat cards from a _guestList_, 
def writeSeatCards(_guestList_, _imgNameBase_, _backgroundImg_, _workDir_):
  from PIL import Image, ImageDraw, ImageFont
  import math
  
  # Calculate drawing size based on cards and paper dimensions
  # Assuming US letter papersize
  ppi = 72 # pixels per inch
  cardWidth = 5 * ppi
  cardHeight = 4 * ppi
  paperWidth = 11 * ppi
  paperHeight = 8.5 * ppi
  # Maximum cards per row in US letter sheet
  cardsPerRow = int(paperWidth / cardWidth)
  # Maximum cards per column in US letter sheet
  cardsPerColumn = int(paperHeight / cardHeight)
  # Maximum cards per US letter sheet
  cardsPerSheet = cardsPerRow * cardsPerColumn
  # Calculate total US letter sheets required
  totalSheets = math.ceil(len(_guestList_) / cardsPerSheet)
  drawingWidth = cardsPerRow * (cardWidth + 1) + 1
  drawingHeight = cardsPerColumn * (cardHeight + 1) + 1
  # print('dwg width: %s' % drawingWidth)
  # print('dwg height: %s' % drawingHeight)

  # Change to working directory
  os.chdir(_workDir_)
  
  # Open background image
  backgroundImage = Image.open(_backgroundImg_)

  # Resize background image to match drawing area
  backgroundImageWidth, backgroundImageHeight = backgroundImage.size
  widthRatio = backgroundImageWidth / cardWidth
  heightRatio = backgroundImageHeight / cardHeight
  resizeFactor = max(widthRatio, heightRatio)
  backgroundImage = backgroundImage.resize(\
      (int(backgroundImageWidth/resizeFactor), \
       int(backgroundImageHeight/resizeFactor)))
  backgroundImageWidth, backgroundImageHeight = backgroundImage.size

  cardCounter = 0
  # Loop through sheets in sheet count
  for paperSheet in range (0, totalSheets):
    
    # Create draw object
    img = Image.new('RGBA', (drawingWidth, drawingHeight), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw grid
    draw.rectangle([0, 0, drawingWidth-1, drawingHeight-1], outline='black')
    for i in range(1, cardsPerRow):
      draw.line([(0, i * (cardHeight + 1)), \
                   (drawingWidth, i* (cardHeight + 1))], \
                fill='blue')      
    for j in range(1, cardsPerColumn):    
      draw.line([(i * (cardWidth + 1), 0), \
                 (i * (cardWidth + 1), drawingHeight)], \
                fill='blue')
  
    # Loop through rows and columns 
    for i in range(cardsPerRow):
      if cardCounter >= len(_guestList_):
        break
      for j in range(cardsPerColumn):
        if cardCounter >= len(_guestList_):
          break
        # Paste backgroun
        img.paste(backgroundImage, (i * (cardWidth + 1) + \
                                    int((cardWidth - backgroundImageWidth)/2), \
                                    j * (cardHeight + 1) + 1))

        # Draw text with guests names on each card
        arialFont = ImageFont.truetype('arial.ttf', 48)
        draw.text((i * (cardWidth + 1) + int(cardWidth / 4), \
                   j * (cardHeight + 1) + int(cardHeight * .8)), \
                   _guestList_[cardCounter] , fill='purple', font=arialFont)
        cardCounter += 1

    # Save image file   
    img.save(_imgNameBase_ + str(paperSheet) + '.png')

# This function reads the guests list from guest list file _fileName_    
def readList(_fileName_):
  # Reads guests list from txt file
  readFile = open(_fileName_)
  linesList = readFile.readlines()
  return linesList

import os

# User can update the arguments passed to the writeSeatCards function below
myFileListName = 'guests.txt'
myGuestList = readList(myFileListName)
imgNameBase = 'seatCard'
# Make sure the name of the image to be used as background is passed here
backgroundImg = 'flower.png'
workDir = os.getcwd()

writeSeatCards(myGuestList, imgNameBase, backgroundImg, workDir)
