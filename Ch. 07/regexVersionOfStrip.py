#! python3
# Automate Boring Stuff Practice Project - Chapter 7
# regexVersionOfStrip.py - removes the characters specified in the second 
# argument from a string, if no arguments are passed then it removes whitespaces

import re

def stripRegexTool(inputString, stripChars):
  if stripChars != '':
    stripRegex = re.compile(r'^(' + stripChars + r')+(.*?)(' + stripChars + r')+$')
    # important .*? nongreedy usage for group 2 means minimum set of
    # characters that meet the pattern criteria
  else:
    stripRegex = re.compile(r'^(\s+)(.*?)(\s+)$')
  inputString = stripRegex.sub(r'\2',inputString)
  return inputString

print('Enter your string:')
testString = input()
print('Enter your strip characters')
testChars = input()
newString = stripRegexTool(testString, testChars)
print('This is your new string:\n%s' % newString)
