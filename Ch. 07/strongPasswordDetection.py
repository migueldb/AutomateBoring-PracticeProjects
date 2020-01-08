#! python3
# Automate Boring Stuff Practice Project - Chapter 7
# strongPasswordDetection.py - uses regular expressions to make sure the 
# password string it is passed is strong. A strong password is defined as one
# that is at least eight characters long, contains both uppercase and lowercase
#characters, and has at least one digit.

import re

lenRegex = re.compile(r'(\S{8})(\S)*$')
upperCaseRegex = re.compile(r'[A-Z]+')
lowerCaseRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'[0-9]+')

print('Enter your password:')
testString = input()
if lenRegex.search(testString) != None and upperCaseRegex.search(testString) != None and lowerCaseRegex.search(testString) != None and digitRegex.search(testString) != None:
  print('This is a strong password')
else:
  print('This is not a strong password')
