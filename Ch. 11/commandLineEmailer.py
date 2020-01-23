#! python3
# Automate Boring Stuff Practice Project - Chapter 16
# commandLineEmailer.py -  takes an email address and string of text on the
# command line and then, using Selenium, logs into your email account and sends
# an email of the string to the provided address
#
# NOTE: This script uses Selenium, please read the installation instructions at:
#       https://selenium-python.readthedocs.io/installation.html
#       This code was tested with Firefox but other browsers can be used.
#       Please check the selenium documentation on how to install the
#       corresponding driver.
#       For safety, the getpass module is used to handle password entry.  User
#       input is required
#
# USAGE: From comandLineEmailer.py directory type on the command prompt:
# C:\path\to\python\py.exe commandLineEmailer.py <recipient's email> message


from selenium import webdriver
import getpass, time, sys

# User is required to input the following variables using the getpass module for
# safety

email = getpass.getpass('Enter your email address:')
pwd = getpass.getpass('Enter your password:')
subject = 'Testing selenium'
toAddress = sys.argv[1]
message = sys.argv[2:]

# Adjust the wait time as required if the page takes time to fully load
waitTime = 3

# Create browser object
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')

# Click on sign-in button
linkElem = browser.find_element_by_link_text('Sign in')
linkElem.click()
time.sleep(waitTime)      # wait for the webpage to load

# Enter email address in login page
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(email)
linkElem = browser.find_element_by_id('login-signin') 
linkElem.click()
time.sleep(waitTime)       # wait for the webpage to load

# Enter password
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys(pwd)
#passwordElem.submit()
linkElem = browser.find_element_by_id('login-signin')
linkElem.click()
time.sleep(waitTime)       # wait for the webpage to load

# Click on "Compose" button
XPATH1 = '//*[@data-test-id="compose-button"]'
linkElem = browser.find_element_by_xpath(XPATH1)
linkElem.click()
time.sleep(waitTime)       # wait for the webpage to load

# Enter recipient's address
toElem = browser.find_element_by_id('message-to-field')
toElem.send_keys(toAddress)

# Enter subject
XPATH2 = '//*[@data-test-id="compose-subject"]'
subjectElem = browser.find_element_by_xpath(XPATH2)
#subjectElem = browser.find_element_by_id('compose-subject')
subjectElem.send_keys(subject)

# Enter message
XPATH3 = '//*[@data-test-id="rte"]'
rteElem = browser.find_element_by_xpath(XPATH3)
#rteElem = browser.find_element_by_id('rte')
rteElem.send_keys(' '.join(message))

# Click on "Send" button
XPATH4 = '//*[@data-test-id="compose-send-button"]'
sendElem = browser.find_element_by_xpath(XPATH4)
sendElem.click()
time.sleep(waitTime)       # wait for the webpage to load

# Close browser
browser.quit()
