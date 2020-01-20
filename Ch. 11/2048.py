#! python3
# Automate Boring Stuff Practice Project - Chapter 11
# 2048.py - Plays 2048 by sending a succesion of keys until the site updates to "game over"
#
# NOTE: This script uses Selenium, please read the installation instructions at:
# https://selenium-python.readthedocs.io/installation.html
# This code was tested with Firefox but other browsers can be used.  Please check
# the selenium documentation on how to install the corresponding driver.
#                     
# See: https://developer.mozilla.org/en-US/docs/Learn/HTML/
#      Forms/Sending_and_retrieving_form_data


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Check if the game is over so the script stops sending keystrokes
def gameOver(browser, theXPATH):
    gO = True
    try:
        # If theXPATH element is found then the game is over
        l = browser.find_element_by_xpath(theXPATH)
        print('Game Over')
    except:
        # If not game over yet, continue and print 'Game On'
        gO = False
        print('Game On')
        browser.refresh
    return gO


def play2048(url,mXPATH):
    # Adjust the wait time as required if the page takes time to fully load
    waitTime = 0.05
    # Create the browser object
    b = webdriver.Firefox()
    #b = webdriver.Opera()
    b.get(url)
    # This selects any part of the screen as everything displayed is under html tag
    htmlElem = b.find_element_by_tag_name('html')
    
    # Send Up, Right, Down, Left keystrokes while not game over yet
    while gameOver(b, mXPATH) == False:
        htmlElem.send_keys(Keys.UP)
        time.sleep(waitTime)
        htmlElem.send_keys(Keys.RIGHT)
        time.sleep(waitTime)
        htmlElem.send_keys(Keys.DOWN)
        time.sleep(waitTime)
        htmlElem.send_keys(Keys.LEFT)
        time.sleep(waitTime)
        
url2048 = 'https://gabrielecirulli.github.io/2048/'
myXPATH = "//*[@class='game-message game-over']"
play2048(url2048, myXPATH)
