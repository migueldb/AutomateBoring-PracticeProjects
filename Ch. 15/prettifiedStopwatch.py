#! python3
# Automate Boring Stuff Practice Project - Chapter 15
# prettifiedStopwatch.py - A simple stopwatch program with prettified output.
#
# NOTE: This script requires pyperclip module to be installed.  See:
#       https://pypi.org/project/pyperclip/
#       for more information

import time
import pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. \
Press Ctrl-C to quit')
# Read user's input (it won't move to the next instruction until the user sends
# ENTER
input()
# Notify the user about the stopwatch having started
print('Started.')
# Read the current time and save it as startTime
startTime = time.time()
# Create with lastTime variable with the startTime value for the moment
lastTime = startTime
lapNum = 1
width = 6
text = ''
# Start tracking the lap times.
try:
  while True:
    # Read user's input (it won't move to the next instruction until the user
    # sends ENTER
    input()
    # lapTime equals current time minus lastTime (startTime for the first lap
    lapTime = round(time.time() - lastTime, 2)
    # totalTime equals current time  minus startTime
    totalTime = round(time.time() - startTime, 2)
    # print lap number, total time and lap time
    print('Lap # %s: %s (%s)' % (str(lapNum).ljust(width), \
                                str(totalTime).center(width), \
                                str(lapTime).rjust(width)), end='')
    # Append new laps to the text to be displayed
    text += 'Lap # %s: %s (%s) \n' % (str(lapNum).ljust(width), \
                                str(totalTime).center(width), \
                                str(lapTime).rjust(width))   
    # Increase lap number
    lapNum += 1
    # Record time at the end of the lap
    lastTime = time.time() # reset the last lap time
# If the user clicks on Ctrl-C, instead of interrupting with error, proceed with
# stoppint the stopwatch and printing Done.
except KeyboardInterrupt:
  # Handle the Ctrl-C exception to keep its error message from displaying.
  print('\nDone.')
# Copy the laps' summary to the clipboard
pyperclip.copy(text)
