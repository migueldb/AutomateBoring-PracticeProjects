#! python3
# Automate Boring Stuff Practice Project - Chapter 11
# imageSiteDownloader2.py - Searches for images based on user provided search queries using
# submitted to any website with search functionality ('/search'), then opens evey link
# provided by the website in response and downloads the images and saves them to a local
# folder.
#
# NOTE: This script uses Selenium, please read the installation instructions at:
# https://selenium-python.readthedocs.io/installation.html
# This code was tested with Firefox but other browsers can be used.  Please check
# the selenium documentation on how to install the corresponding driver.
#                     
# See: https://developer.mozilla.org/en-US/docs/Learn/HTML/
#      Forms/Sending_and_retrieving_form_data

from selenium import webdriver
import requests
import os, bs4

# User is require to import the image search website address below
website = 'https://imgur.com/'
##website = 'https://flickr.com'

# Enter the search query below
searchQuery = 'parrots'

# Concatenate website address and search term to complete the URL
url = website + '/search?q=' + searchQuery

# Create browser object
# On a side note:  requests and urllib modules proved unable to obtain the correct responses
# from the server unlike selenium 
browser = webdriver.Firefox()
browser.get(url)

# Create the SOAP object and close browser
s = bs4.BeautifulSoup(browser.page_source, 'lxml')
browser.quit()

# Save response to an HTML file (optional)
htmlFile = open('htmlFile.html', 'wb')
htmlFile.write(s.prettify().encode('utf-8'))
htmlFile.close()

# Create the search element (links to images)
linkElem = s.select("body div#content a[href]")

# Print error message if no images are returned
if linkElem == []:
    print("Can't find any corresponding image dude")
else:
    # Create a directory to store the images
    os.makedirs(searchQuery, exist_ok=True)
    
    #Loop through links
    for link in linkElem:
        # Get image webpage address
        shortLink = link.get('href')
        # If address invalid skip next
        if not shortLink.startswith('/'):
            continue
        # Form image webpage full address
        imgPageUrl = website + link.get('href')
        # Open image webpage, skip next if error
        try:
            r = requests.get(imgPageUrl)
            r.raise_for_status()
        except:
            continue
        # Create SOAP object
        s = bs4.BeautifulSoup(r.text, 'lxml')

        # Create the search element for the image 
        imgElem = s.select("body img[src]")

        # If no images found, skip next
        if imgElem == []:
            continue

        # Save image address to variable
        imgUrl = imgElem[0].get('src')
        
        # If image ends with a valid extension proceed to download
        # Add extensions to the list as required
        validExtList = ['.jpg', '.jpeg', '.gif']
        validExtension = True
        for ext in validExtList:            
            if imgUrl.endswith(ext):
                validExtension = True
                break
            else:
                validExtension = False
        if not validExtension:
            continue

        # Check if the url starts with https:
        if not imgUrl.startswith('https:'):
            imgUrl = 'https:' + imgUrl

        # Open image link, skip next if error
        try:
            r = requests.get(imgUrl)
            r.raise_for_status()
        except:
            continue
        # Create image file
        imgFile = open(os.path.join(searchQuery, os.path.basename(imgUrl)), 'wb')
        for chunk in r.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()
        
        # Print current status
        print('Saving file: %s' % imgUrl)








