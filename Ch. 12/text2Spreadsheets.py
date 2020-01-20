#! python3
# Automate Boring Stuff Practice Project - Chapter 12
# text2Spreadsheets.py - reads the contents of all the text files inside in a
#                        given folder and copies them to a spreadsheet, line by
#                        line.  Each column will contain text from a separate
#                        text file.  Each cell will contain a separate line.
#
# NOTE: This script requries a text file saved in the working directory
#

import os
import openpyxl as o

def copyText2SS(_extensions_, _folderPath_):
    # Create workbook object
    wb = o.Workbook()
    # Select active worksheet
    sheet = wb.active
    # Start with column 1
    currCol = 1
    # Loop through all files in the folder
    for entry in os.scandir(_folderPath_):
        # Test if the files are text files
        for ext in _extensions_:
            if entry.name.endswith(ext) and entry.is_file():
                # If a text file is found print a message
                print('found: ' + entry.name)
                # Create a read file object
                readFile = open(os.path.join(_folderPath_, entry.name))
                # Create a list with the text file lines
                linesList = readFile.readlines()
                # Read the text file line by line and write it to the cells in the same column
                # in the spreadsheet
                currRow = 1
                for lines in linesList:
                    # Print a status message
                    print('writing line %s from file: %s' %(currRow, entry.name))
                    sheet.cell(row = currRow, column = currCol).value = lines
                    currRow += 1
                currCol +=1

    # Save spreadsheet
    wb.save('-'.join(_folderPath_.split(os.path.sep))+'.xlsx')


# List of text files extensions
myExtensions = ['.txt', '.csv', '.py', '.bat']
myFolderPath = os.getcwd()
copyText2SS(myExtensions, myFolderPath)
