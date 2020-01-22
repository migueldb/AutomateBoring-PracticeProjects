#! python3
# Automate Boring Stuff Practice Project - Chapter 13
# pdfPwdBreaker.py - Breaks a pdf encryption password using a given list of
# words
#
# NOTE: This script requres the PyPDF2 module to be installed.  See:
#       https://pypi.org/project/PyPDF2/
#       for more details
#       This script also requires a password list in a txt file format.  This
#       file can be downloaded here:
#       https://nostarch.com/download/
#       Automate_the_Boring_Stuff_onlinematerials_v.2.zip

import PyPDF2

# Password breaker callable function
def breakPwd(_wordsList_,_pdfFileName_):
  # Create pdf object
  pdfFileObj = open(_pdfFileName_, 'rb')
  # Create pdf reader object
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  # Check if the pdf file is encrypted
  if pdfReader.isEncrypted == False:
    # File not encrypted: do nothing
    print('This file is not encrypted.  No action taken.')
  else:
    # This line adds the same passwords but this time in lower case to a tuple
    _wordsList_ += [line.lower() for line in _wordsList_]
    wordsTuple = tuple(_wordsList_)
    # Status message
    print('File %s is encrypted, proceeding to decrypt it.' %(_pdfFileName_))
    decrypted = 0
    # Try each of the works in the passwords tuple
    while True:
      for keyWords in wordsTuple:
        key = keyWords
        # Print currenty key being tested
        print('Trying "%s"' %(key))
        decrypted = pdfReader.decrypt(key)
        # Exit for loop if file successfuly decrypted
        if decrypted == 1: # This if statement is necessary as while loop
          break            # will only evaluate after the for loop is completed
      break
    # If the key is not found in the passwords tuple then print a message
    if decrypted == 0:
      print('I could not find the password')
    # If the key is found in the passwords tuple then print a message with the
    # key
    else:
      print('Password found.  The password is: "%s"' %(key))
    
# This function reads the text file with the passwords list
def readList(_fileName_):
  try:
    readFile = open(_fileName_)
    #This ensures the removal of the '\n' new line at the end of each line
    linesList = [line.strip('\n') for line in readFile.readlines()]
  except:
    print("I'm having problems opening the file %s" % _fileName_)
    linesList = []
  return linesList


# User can edit the values below
myWordsListFile = 'dictionary.txt'
# A shorter list for testing
#myWordsListFile = 'shortDict.txt'
myWordsList = readList(myWordsListFile)
myPdfFileName = 'encryptedminutes.pdf'

# Function call
breakPwd(myWordsList, myPdfFileName)
