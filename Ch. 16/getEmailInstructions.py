#! python3
# Automate Boring Stuff Practice Project - Chapter 16
# getEmailInstructions.py - reads email instructions and executes them
#
# NOTE: This script requires the pyzmail module to be installed.  See:
#       https://pypi.org/project/pyzmail/
#       for more information
#
# USAGE: Send an email to my_email_address from senderEmail with subject:
#        subjectPass.  The email body will have the instructions, separated
#        with commas: first the path to the exe file, then the exe file and
#        lastly the arguments.  i.e.:
#        C:\\Program Files (x86)\\Notepad++,notepad++.exe,-qnrandom
#        See subprocess module documentation for more details

# This function gets the instructions from the email.  The email must have
# specified sender _senderEmail_ and subject _subjectPass_
def getInstructions(_senderEmail_, _subjectPass_):
    import imapclient, getpass, pyzmail, datetime

    # User can change the folder where the instructions will be searched
    _folder_ = 'Inbox'
    # Create the imap object.  The user can change the server as required
    imapObj = imapclient.IMAPClient('imap.mail.yahoo.com', ssl=True)

    # Get user and password using getpass module for safety
    my_email_address = getpass.getpass('Enter your email address:')
    MY_SECRET_PASSWORD = getpass.getpass('Enter your password:')
    imapObj.login(my_email_address, MY_SECRET_PASSWORD)
    imapObj.select_folder(_folder_, readonly=False)
    dt = datetime.datetime.now()

    # Find the email with the instructions.  This email is required to meet
    # certain criteria for safety (sender and subject)
    UIDs = imapObj.search(['FROM', '%s' % _senderEmail_, \
                           'SUBJECT', '%s' % _subjectPass_, \
                           'SINCE', '%s' % dt.strftime('%d-%b-%Y'), \
                           'UNSEEN'])
# print('Instuctions found!' if UIDs != [] else "Still waiting on instructions")
    # If instructions are found
    if UIDs != []:
        # Print status message
        print('Instructions found')
        # Fetch email's body
        rawMessages = imapObj.fetch(UIDs, [b'BODY[]'])
        # Get message
        message = pyzmail.PyzMessage.factory(rawMessages[UIDs[0]][b'BODY[]'])
        # Get text part of the message and decode it (it is binary)
        instructionsString = message.text_part.get_payload().\
        decode(message.text_part.charset)
        # Flag the message as read so the instruction is not executed twice
        imapObj.add_flags(UIDs[0], br'\Flagged')
        imapObj.logout()
        # Print instructions string
        print(instructionsString)
        # Remove unnecessary characters from the instructions string
        instructionsString = instructionsString.strip("\r\n")
        # The instruction components are separated by commas: _path_, _exeFile_,
        # _arguments_.  Split the instructions
        instructions = instructionsString.split(',')
    else:
        # If no new instructions found tell the user
        print('Still waiting on new instructions...')
        instructions = []
    return instructions

# This function gets the instructions string and executes it
def executeInstructions(_path_, _exeFile_, _arguments_):
    import subprocess, os
    qbProcess = subprocess.Popen([os.path.join(_path_, _exeFile_), _arguments_])

import getpass

# User must enter the email address from which the instructions will be sent 
senderEmail = getpass.getpass("Enter the sender's email:")
# This is for security, it's intended to prevent others from sending
# instructions
subjectPass = 'Instruction 123456789'

# Get instructions from email by calling the function getInstructions
newInstructions = getInstructions(senderEmail, subjectPass)

# If there are new instuctions, exceute them by calling the function
# executeInstructions
if newInstructions != []:
    path, exeFile, arguments = newInstructions
    print('These are the new instructions: \n')
    print(path, exeFile, arguments)
    executeInstructions(path, exeFile, arguments)
