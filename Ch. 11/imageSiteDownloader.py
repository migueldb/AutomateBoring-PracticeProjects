#! python3
# Automate Boring Stuff Practice Project - Chapter 11
# imageSiteDownloader.py - Searches for images based on user provided search query and
# downloads them from 'https://imgur.com' website.
#
# See: https://developer.mozilla.org/en-US/docs/Learn/HTML/
#      Forms/Sending_and_retrieving_form_data
#
# NOTE: This script requres the Beautiful Soup 4 module to be installed.  See:
#       https://pypi.org/project/beautifulsoup4/
#       for more information

import requests, os, bs4

website = 'https://imgur.com/'

# Enter the search query below
searchQuery = 'parrots'

# Concatenate website address and search term to complete the URL
url = website + 'search'

# This header is a standard Firefox webbrowser header, it helps with preventing
# the website from identifying the scrip as an automatic scraping code and
# retunrning unusable responses
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
query = {'q':searchQuery}

# Create the request object and check for status
r = requests.get(url, params=query, headers=headers)
r.raise_for_status()

# Create a directory to store the images
os.makedirs(searchQuery, exist_ok=True)

# Create the SOUP object
s = bs4.BeautifulSoup(r.text, features='lxml')

# Create the search element (images)
imgElem = s.select('#imagelist img')

# Print error message if no images are returned
if imgElem == []:
    print("Can't find it dude")
else:

    #Loop through every image element and download the image
    for i in range(len(imgElem)):
        imgUrl = 'http:' + imgElem[i].get('src')
        r = requests.get(imgUrl)
        r.raise_for_status()
        imgFile = open(os.path.join(searchQuery, os.path.basename(imgUrl)), 'wb')
        for chunk in r.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()
