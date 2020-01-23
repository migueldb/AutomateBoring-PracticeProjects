#! python3
# Automate Boring Stuff Practice Project - Chapter 18
# lookingBusy.py - nudges the mouse cursor every few minutes.
#
# NOTE: This script uses PyAutoGUI module.  Please see installation instructions
#       here: https://pyautogui.readthedocs.io/en/latest/install.html
#

# This function nudges the mouse a small magintude that doesn't interfere with
# normal working
def nudgeTheMouse():
    import pyautogui
    # The magnitude can be adjusted (this how far the mouse will nudge)
    magnitude = 100
    # Print a notification
    print('Nudge!')
    # Move the mouse in a square patern landing at the same starting point
    pyautogui.moveRel(magnitude, 0)
    pyautogui.moveRel(0,magnitude, 0)
    pyautogui.moveRel(-magnitude,0, 0)
    pyautogui.moveRel(0,-magnitude, 0)

# Using threading
import threading, time
# The user can modify the interval
interval = 0.1           # interval in minutes
intervalInSeconds = interval*60

# Use try and except to have the option to exit with CTRL + C
try:
    while True:
        # Create a new thread with the nudgeTheMouse function
        threadObj = threading.Thread(target=nudgeTheMouse)
        # Print instructions
        print('\n>>> Next nudge in %s seconds press CTRL + C to interrupt <<<\n' % \
              intervalInSeconds)
        # Wait
        time.sleep(intervalInSeconds)
        threadObj.start()
        threadObj.join()
        threadObj = None
except KeyboardInterrupt:
    print('CTRL + C')
