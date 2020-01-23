#! python3
# Automate Boring Stuff Practice Project - Chapter 16
# autoUnsubscriber.py - Gets the unsuscribe links from emails and opens them in
# a browser
#
# NOTE: This script requres the Beautiful Soup 4 module to be installed.  See:
#       https://pypi.org/project/beautifulsoup4/
#       for more information.
#       This script requires the pyzmail module to be installed.  See:
#       https://pypi.org/project/pyzmail/
#       for more information
#       For safety, the getpass module is used to handle password entry.  User
#       input is required

# This function opens the links provided in the list _linksList_
def openLinks(_linksList_):
  import webbrowser

  # Loop through every link in _linksList_
  for link in _linksList_:
    webbrowser.open(link)


# This fuction gets the unsubscribe links from the emails stored in _folder_
def getUnsubscribeLinks(_folder_):
  import imapclient, getpass, sys, pyzmail, bs4

  # Create the imapclient object
  imapObj = imapclient.IMAPClient('imap.mail.yahoo.com', ssl=True)
  
  # Get user and password using getpass module for safety
  my_email_address = getpass.getpass('Enter your email address:')
  MY_SECRET_PASSWORD = getpass.getpass('Enter your password:')

  # Login
  imapObj.login(my_email_address, MY_SECRET_PASSWORD)

  # Change to folder
  imapObj.select_folder(_folder_, readonly=True)
  # Search all emails in _folder_
  UIDs = imapObj.search('ALL')
  # fetch all the bodies from all the emails in _folder_
  rawMessages = imapObj.fetch(UIDs, [b'BODY[]'])
  # Createa list to store the unsubscribe links
  linksList = []
  # Loop through every string in the email bodies list
  for seq in rawMessages:
    # Get the message's html part
    message = pyzmail.PyzMessage.factory(rawMessages[seq][b'BODY[]'])
    # If no html part then continue to the next email body
    if message.html_part == None:
      continue
    # Decode the message part.  It is binary
    text = message.html_part.get_payload().decode(message.html_part.charset)
    # Create the SOUP object
    soup = bs4.BeautifulSoup(text, features='lxml')

    # Create a list with the search criteria for unsubscribe link
    unsubscribeElem = soup.find_all("a", string=["Unsubscribe", \
                                                 "Unsubscribe/Modify", \
                                                 "unsubscribe", "UNSUBSCRIBE"])
    # If no email body meets the criteria tell the user
    if unsubscribeElem == []:
      print('No unsubscribe link in mail %s' % seq)
    else:
      # Otherwise add the link to the links list
      linksList.append(unsubscribeElem[0].get('href'))

  # Return list
  return linksList
  

# User can change the email folder name if required
folder = 'Inbox'
# Get the links list by calling the function getUnsubscribeLinks
myLinksList = getUnsubscribeLinks(folder)
# Optional if the user requires the list with the links
#print(myLinksList)

# Open all the links in the links list to unsubscribe
openLinks(myLinksList)
