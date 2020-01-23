#! python3
# Automate Boring Stuff Practice Project - Chapter 16
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string required by umbrellaRemainder.py
#
# NOTE: This script requires a twilio account in order to send automated text
#       messsages.  Please see the link below for more infomation:
#       https://www.twilio.com/try-twilio
#       For safety, the getpass module is used to handle password entry.  User
#       input is required
#       

import getpass

# Preset values, require user input
accountSID = getpass.getpass('Enter account SID:')
authToken = getpass.getpass('Enter authorization token:')
myNumber = getpass.getpass('Enter your cellphone number in this format +xxxxxxxxxx: ')
twilioNumber = getpass.getpass('Enter Twilio number')

from twilio.rest import Client

def textmyself(message):
  twilioCli = Client(accountSID, authToken)
  twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
