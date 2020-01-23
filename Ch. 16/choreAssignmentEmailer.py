#! python3
# Automate Boring Stuff Practice Project - Chapter 16
# choreAssignmentEmailer.py - sends chores from a list to a list of email 
# recipients.
#
# NOTE: This script requires smtplib module to be installed.
#       For safety, the getpass module is used to handle password entry.  User
#       input is required
#       Some email services require automation apps to be registered and have
#       application specific passwords.  Please see more information below:
#       https://help.yahoo.com/kb/SLN15241.html

# This function creates the text string to be emailed from two string variables
# that fit into a message string
def emailStringFromChore(_name_, _chore_):
  _body_ = "Subject: You've been assined a chore.\n\nDear Chore taker: %s,\n\
  Thanks for volunteering to take chores with us.  This week's chore is: %s\n\
  Enjoy.\nRegards,\nThe Chore Admin." % (_name_, _chore_) 
  return _body_

# This function assigns random chores from __choresList__ to each of the
# recipients in __choresList__
def choreAssigner(__emailAddressDict__, __choresList__):
  import random, os, pprint
  # The names, emails and current chores assigned will be stored in a dictionary
  # in choresReg.py so previously assigned chores can be checked to prevent
  # chores assignment repetition
  choresRegister = 'choresReg.py'
  registerLocation = os.getcwd()
  # If the dictionary with names, emails and chores still doesn't exist then
  # create one, this means there have not been chores previously assigned to
  # anyone.  Otherwise store the previously assigned chores in
  # assignedChoresDict
  try:
    import choresReg
    assignedChoresDict = choresReg.Register
  except:
    print('the file %s has not been created yet' % choresRegister)
    assignedChoresDict = {}
 
  # Print a message with the dictionary before new chores are assigned
  print('This is the current chores register:')
  print(assignedChoresDict)
    
  # Loop through names in the keys of the dictionary with name and emails
  for name in __emailAddressDict__.keys():
    # Get a random chore from the list of chores
    randomChore = random.choice(__choresList__)
    # Instert new keys to the names, emails and chores dictionary if they don't
    # exits yet.  Assign values to the new keys.
    assignedChoresDict.setdefault(name, {'email': __emailAddressDict__[name], \
                                         'newChore': randomChore, \
                                         'oldChore': ''})
    # If there was no chore assigned previously then assign the random chore
    # already selected from the chores list, 
    if assignedChoresDict[name]['oldChore'] != '':
      # Keep looping through the chores list until a not previously assigned
      # chores is found
      while assignedChoresDict[name]['newChore'] == randomChore:
        randomChore = random.choice(__choresList__)
    # Once a new, not previously assigned chore is found, the current chore
    # becomes oldChore and the new random chore found becones newChore
    assignedChoresDict[name]['oldChore'] = assignedChoresDict[name]['newChore']
    assignedChoresDict[name]['newChore'] = randomChore
  
  # Save chores register (where the names, emails and chores dictionary are
  # saved
  print('Writing chores register...')
  registerFile = open(os.path.join(registerLocation, choresRegister), 'w')
  registerFile.write('Register = ' + pprint.pformat(assignedChoresDict))
  registerFile.close()
  print('Done.')

  # Return the updated dictionary
  return assignedChoresDict

# This function sends and email to _emailAddressDict_ with the personalized
# message
def assignmentEmailSender(_emailAddressDict_, _choresList_):
  import smtplib, getpass
  
  # Loging to email account
  # The user can set up other email servers if required
  smtpObj = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
  #smtpObj.set_debuglevel(1)
  smtpObj.ehlo()

  # Get user and password using getpass module for safety
  my_email_address = getpass.getpass('Enter your email address:')
  MY_SECRET_PASSWORD = getpass.getpass('Enter your password:')
  smtpObj.login(my_email_address, MY_SECRET_PASSWORD, initial_response_ok=True)

  # Send out emails
  # First call the choreAssigner function to get new chores for each name
  newRegister = choreAssigner(_emailAddressDict_, _choresList_)

  # Loop through names in the names, emails and chores dictionary
  for name in newRegister.keys():
    # Get the email body by calling the emailStringFromChore function
    body = emailStringFromChore(name, newRegister[name]['newChore'])
    email = newRegister[name]['email']
    # Status message
    print('Sending email to: %s' % (email))
    # Send email and get status from server
    sendMailStatus = smtpObj.sendmail(my_email_address, email, body)

    # Communicate status to user
    if sendMailStatus != {}:
      print('There was a problem sending the email to %s: %s' % (email, \
                                                                sendmailStatus))                                                                
  # Close connection with server                                                              sendmailStatus))
  smtpObj.quit()

# User can add, remove chroes from the following list
chores = ['dishes', \
          'bathroom', \
          'vacuum', \
          'walk dog']

# User can add, remove names and emails from the following dictionary
emailAddressDict = {'Charles Example': 'charles@example.com',
                    'Mike Example': 'mike@example.com',
                    'Alice Example': 'alice@example.com',
                    'Bob Example': 'bob@example.com'}

# Fucntion call
assignmentEmailSender(emailAddressDict, chores)
