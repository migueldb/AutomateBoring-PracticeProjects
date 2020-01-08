#! python3
# Automate Boring Stuff Practice Project - Chapter 8
# madLibs.py - reads in text files and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
#
# create a text file with the following text:
'''
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
'''
# and save it as madlib.txt in the work directory.  The createTXT function can
# be used to create madlib.txt

import re, os

def createTXT(_string_,_fileName_):
    if _fileName_ not in os.listdir(os.getcwd()):
        print('No madlib.txt file.  Proceeding to create one')
        textFile = open(_fileName_, 'w')
        textFile.write(_string_)
        textFile.close

def replaceWords(adj, noun1, verb, noun2):
  newWords = [adj, noun1, verb, noun2]
  testFile = open('madlib.txt')
  testString = testFile.read()
  originalString = testString
  testFile.close()
  keyWords = ['ADJECTIVE','NOUN', 'VERB', 'NOUN']
  for i in range(len(keyWords)):
    replaceRegex = re.compile(keyWords[i])
    testString = replaceRegex.sub(newWords[i], testString, count=1)

  newFileName = 'newmadlib.txt'
  if newFileName in os.listdir(os.getcwd()):
    print('%s file already exists.  Overwriting' % newFileName)

  print('the following string: ', '"', originalString, '",')
  print('will be replaced with this string: ', '"', testString, '".' )

  newFile = open(newFileName, 'w')
  newFile.write(testString)
  newFile.close()

myString = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN\
 was unaffected by these events.'
myFileName = 'madlib.txt'
createTXT(myString, myFileName)



print('Enter and adjective:')
adjective = input()
print('Enter a noun:')
noun1 = input()
print('Enter a verb:')
verb = input()
print('Enter a noun:')
noun2 = input()
replaceWords(adjective, noun1, verb, noun2)
