#! python3
# instantMessengerBot.py - sends out a notification message to a group over
# over Skype.
# NOTE: This script uses PyAutoGUI module.  Please see installation instructions
#       here: https://pyautogui.readthedocs.io/en/latest/install.html
#       This file requres a screenshot of the Skype search box saved in the
#       working directory as skypeSearchBox.png and a screenshot of the close
#       window button saved as closeWindowButton.png.  Examples are provided in
#       this directory.

def sendMessage(_name_,_message_):
    import pyautogui

    pyautogui.PAUSE = 0.25  # Interval between pyautogui commands
    _interval_ = 0.5       # Typing interval
    

    
    # Find search box location and click on it
    searchBoxImg = 'skypeSearchBox.png'
    searchBoxCoord = pyautogui.locateOnScreen(searchBoxImg)
    print(searchBoxCoord)
    searchBoxCenter = pyautogui.center(searchBoxCoord)
    print(searchBoxCenter)
    pyautogui.rightClick(searchBoxCenter)       # Remember left-hand mouse

    # Type friend's name and open message window
    
    pyautogui.typewrite(_name_, interval = _interval_)
    pyautogui.press('enter', presses=3, interval = _interval_)
    
    # Type message
    pyautogui.typewrite(_message_, interval = _interval_)
    pyautogui.press('enter')

    # Close message window
    closeWindowImg = 'closeWindowButton.png'
    closeWindowCoord = pyautogui.locateOnScreen(closeWindowImg)
    print(closeWindowCoord)
    closeWindowCenter = pyautogui.center(closeWindowCoord)
    print(closeWindowCenter)
    pyautogui.rightClick(closeWindowCenter)     # Remember left-hand mouse

    # Clear the search box
    pyautogui.press('esc', presses=2, interval = _interval_)

# The user can update the arguments below to be passed to the sendMessage
# function
namesList = ['name1', 'name2']
message = '(hearteyesdog)'

##sendMessage(namesList[0], message)

for name in namesList:
    sendMessage(name, message)
