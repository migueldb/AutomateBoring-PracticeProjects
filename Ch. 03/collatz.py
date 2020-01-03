#! python3
# Automate Boring Stuff Practice Project - Chapter 3
# collatz.py - Generates a Collatz sequence of numbers starting from a user
# provided integer


def collatz(number):
  if number % 2 == 0:
    print(number // 2)
    return (number // 2)
  elif number % 2 == 1:
    print(3 * number + 1)
    return (3 * number + 1)
 
collatzNumber = 1
print('Enter number: (Do not be shy, you can pick a very very big number')
try:
    collatzNumber = int(input())
except ValueError:
    print('Error: the value entered is not an integer number.')
while collatzNumber != 1:
  collatzNumber = collatz(collatzNumber)
print('The Collatz sequence has been completed')
