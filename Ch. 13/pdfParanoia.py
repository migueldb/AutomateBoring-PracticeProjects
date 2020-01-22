#! python3
# Automate Boring Stuff Practice Project - Chapter 13
# pdfParanoia.py - Encrypts all the pdf files in a folder including subfolders
#
# NOTE: This script requres the PyPDF2 module to be installed.  See:
#       https://pypi.org/project/PyPDF2/
#       for more details

import os, PyPDF2

# This function encrypts the pdf files located in _folder_, the encrypted files
# are saved with a new name composed by the old file name plus a given suffix
# _suffix_, the encryption key is provided with the variable _key_
def encryptPDFs(_folder_, _suffix_, _key_):
    _folder_ = os.path.abspath(_folder_) # make sure _folder_ is absolute
    # Create the pdf writer object
    pdfWriter = PyPDF2.PdfFileWriter()
    # Walk through folders and subfolders
    for foldername, subfolders, filenames in os.walk(_folder_):
      # Show the current folder being analyzed
      print('Encrypting files in %s...' %(foldername))
      # Check for pdf files in current folder
      for filename in filenames:
        if filename.endswith('.pdf'):
          # Open each pdf file found (create pdf reader object)
          pdfFileObj = open(os.path.join(foldername, filename), 'rb')
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
          # Skip pdf files already encrypted
          if pdfReader.isEncrypted == True:
            print('File %s is encrypted, skip forward.' %(filename))
            continue
          # Copy the pdf file pages, one by one, from the reader to the writer
          for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
          # At the end encrypt the pdf writer object
          pdfWriter.encrypt(_key_)
          # Save the pdf writer object to a new pdf file with suffix showing
          # it was encrypted
          resultPdf = open(os.path.join(foldername, \
                           os.path.splitext(filename)[0] + _suffix_), 'wb')
          pdfWriter.write(resultPdf)
          # Close files
          resultPdf.close()
          pdfFileObj.close()
          
# This function decrypts the pdf files located in _folder_, the decrypted files
# are saved with a new name composed by the old file name plus a given suffix
# _suffix_, the encryption key is provided with the variable _key_
def decryptPDFs(_folder_, _suffix_, _key_):
    _folder_ = os.path.abspath(_folder_) # make sure _folder_ is absolute
    # Create the pdf writer object
    pdfWriter = PyPDF2.PdfFileWriter()
    # Walk through folders and subfolders
    for foldername, subfolders, filenames in os.walk(_folder_):
      # Show the current folder being analyzed
      print('Decrypting files in %s...' %(foldername))
      # Check for pdf files in current folder
      for filename in filenames:
        if filename.endswith('.pdf'):
          # Open each pdf file found (create pdf reader object)
          pdfFileObj = open(os.path.join(foldername, filename), 'rb')
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
          # Check if the file is encrypted
          if pdfReader.isEncrypted == True:
            print('File %s is encrypted, proceeding to decrypt it' %(filename))
            # Decrypt file
            pdfReader.decrypt(_key_)
            # Copy the pdf file pages, one by one, from the reader to the writer
            for pageNum in range(pdfReader.numPages):
              pageObj = pdfReader.getPage(pageNum)
              pdfWriter.addPage(pageObj)
            # Save the pdf writer object to a new pdf file with suffix showing
            # it was decrypted
            resultPdf = open(os.path.join(foldername, \
                             os.path.splitext(filename)[0] + _suffix_), 'wb')
            pdfWriter.write(resultPdf)
            # Close files
            resultPdf.close()
            pdfFileObj.close()


# User can modify the folder location, suffixes and keys as required
myFolder = os.getcwd()
mySuffix1 = '_encrypted.pdf'
mySuffix2 = '_decrypted.pdf'
myKey = '12345'

# Call functions
encryptPDFs(myFolder, mySuffix1, myKey)
decryptPDFs(myFolder, mySuffix2, myKey)
