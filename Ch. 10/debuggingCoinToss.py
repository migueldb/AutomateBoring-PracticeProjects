#! python3
# Automate Boring Stuff Practice Project - Chapter 10
# debuggingCoinToss.py - The objective of this practice project is to use the
# debugging functions to fix the code provided.  The original code follows.

'''
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
'''

import random, logging
logging.basicConfig(level=logging.DEBUG, \
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

answers = {0: 'tails', 1: 'heads'}

guess = ''
while guess not in ('heads', 'tails'):
  print('Guess the coin toss! Enter heads or tails:')
  guess = input()
  assert guess in ('heads', 'tails'), 'User entered invalid word'
toss = answers[random.randint(0,1)] # 0 if tails, 1 if heads
logging.debug('Right answer is: ' + str(toss))

if toss == guess:
  print('You got it!')
else:
  print('Nope! Guess again!')
  guess = input()
  if toss == guess:
    print('You got it!')
  else:
    print('Nope.  Your are really bad at this game.')
