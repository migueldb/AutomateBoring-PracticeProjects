#! python3
# Automate Boring Stuff Practice Project - Chapter 12
# blankRowInserter.py - Insters M rows starting at row N in an excel file.
#
# NOTE: This script requries a spreadsheet file saved in the working directory
#
# USAGE: From blankRowInserter.py directory type on the command prompt:
# C:\path\to\python\py.exe blankRowInserter.py <start at row> <number of rows to insert>
# <filename>, i.e.
# py blankRowInserter.py 3 2 multiplicationTable6.xlsx


import openpyxl as o
import sys


def insertRows(_N_,_M_,_sheetNumber_,_fileName_):
  # Create workbook object
  wb = o.load_workbook(_fileName_)
  # Select the given worksheet by number
  sheet = wb.worksheets[_sheetNumber_-1]
  # Insert M rows starting at row N
  sheet.insert_rows(_N_,_M_)
  # Save the worksheet with a new name
  wb.save('insert'+_fileName_)

N = int(sys.argv[1])
M = int(sys.argv[2])
sheetNumber = 1
fileName = str(sys.argv[3])
insertRows(N,M,sheetNumber,fileName)
