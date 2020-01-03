#! python3
# Automate Boring Stuff Practice Project - Chapter 4
# commaCode.py - Takes a list and returns a string with comma-separated items.

def returnString(inputList):
  newString = inputList[0]
  for i in range(1,len(inputList)-1):
    newString = newString + ', ' + inputList[i]
  newString = newString + ' and ' + inputList[len(inputList)-1]
  return newString

spam = ['apples', 'bananas', 'tofu', 'cats']
print("Here's the list:")
print(spam)
print("Here's the string:")
print(returnString(spam))
