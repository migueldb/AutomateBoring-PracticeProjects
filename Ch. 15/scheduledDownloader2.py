#! python3
# Automate Boring Stuff Practice Project - Chapter 15
# scheduledDownloader.py - Checks for new images since last visit to multiple
#                          comics websites
#
# NOTE: This script requres the Beautiful Soup 4 module to be installed.  See:
#       https://pypi.org/project/beautifulsoup4/
#       for more information
#       This script is intended to be launched by the operating system’s
#       scheduler (Scheduled Tasks on Windows, launchd on OS X, and cron on
#       Linux).  Refer to the corresponding scheduler documentation on how to
#       run scripts on schedule.
#       An example of the comics websites list can be found here:
#       https://nostarch.com/download/
#       Automate_the_Boring_Stuff_onlinematerials_v.2.zip      

import requests, os, bs4

# Callable function, it checks for new comics at _url_ that are not already
# saved at specific comic folder inside folder _rootFolderName_
def downloadNewImages(_url_,_rootFolderName_):

    # Change work folder
    os.chdir(_rootFolderName_)

    # Print status: Downloading the page...
    print('Downloading page %s...' % (_url_))

    # This header is a standard Firefox webbrowser header, it helps with
    # preventing the website from identifying the scrip as an automatic
    # scraping code and retunrning unusable responses
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    # Create the request object and check for status
    res = requests.get(_url_, headers=headers)
    res.raise_for_status()

    # remove http:// and / to create the comics folder name
    _url_ = _url_.rstrip('/').lstrip('http://')
    os.makedirs(_url_, exist_ok=True)
    
    # Create the SOUP object
    soup = bs4.BeautifulSoup(res.text, features='lxml')

    # Find the URL with the comic image.
    # List of search criteria.  USER can add as required.
    # ^= starts with, ,$= ends with, *= contains
    comicElemList = ['body div[id*="comic"] img[alt]',
                     'body div[id*="content"] img[alt]',
                     'body div[id*="main"] img[alt]',
                     'body div[class*="main"] img[alt]']

    # Loop through each search criterium
    comicElem = []
    for elem in comicElemList:
        thisComicElem = soup.select(elem)
        if not thisComicElem == []:
            comicElem = thisComicElem
            break

    # Print error message if no url meets the search criteria
    if comicElem == []:
        print('Could not find comic image at this URL: %s' %(_url_))
    else:
        
        # Remove repeated elements from comicElem
        comicElem = list(dict.fromkeys(comicElem))
        # Loop through comic elements found        
        for elem in comicElem:
            # Manage errors with exceptions
            try:
                # Get the first link with image
                #comicUrl =''
                comicUrlString = elem.get('src')
                urlBegining1 = 'http://'
                urlBegining2 = 'https://'
                urlBegining3 = '/'
                # Check if the url starts with http:// or https://, add if
                # needed
                if comicUrlString.startswith(urlBegining1) or \
                   comicUrlString.startswith(urlBegining2):
                    comicUrl = comicUrlString
                else:
                    if comicUrlString.startswith(urlBegining3):
                        #continue
                        comicUrl = urlBegining1 + _url_ + comicUrlString
                    else:
                        if ".com" in comicUrl:
                            comicUrl = urlBegining1 + comicUrlString
                        else:
                            comicUrl = url + comicUrlString

                # If comicUrl has extra characters after extension starting with
                # ?
                if "?" in comicUrl:
                    comicUrl = comicUrl[:comicUrl.index("?")]

                # Form the image base name
                fileBasename = os.path.basename(comicUrl)

                # If comicUrl is invalid continue
                if comicUrl == '':
                    continue
                if "." not in fileBasename:
                    continue
                
                # Print status message: Download the image.            
                print('Downloading image %s...' % (comicUrl))
                res = requests.get(comicUrl, headers=headers)
                res.raise_for_status()
                
            except:
                print('Error while downloading the comic')
                continue

            filesList = os.listdir(_url_)
            # If the corresponding base name image has not been stored yet proceed
            # to store it as a new image in the folder
            if fileBasename not in filesList:
                # Create image file object
                imageFile = open(os.path.join(_url_, fileBasename), 'wb')
                # Save the image chunk by chunk
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                # Close the image
                imageFile.close()

# User can change the folder name as required and add new comics url to urlList
rootFolderName = os.getcwd()
urlList = ['http://www.lefthandedtoons.com/',
           'http://buttersafe.com/',
           'http://www.savagechickens.com/',
           'http://www.lunarbaboon.com/',
           'http://completelyseriouscomics.com/',
           'http://www.exocomics.com/',
           'http://nonadventures.com/',
           'http://moonbeard.com/',
           'http://www.happletea.com/']

# Loop through urls in urlList and call the downloader function
for url in urlList:
    downloadNewImages(url, rootFolderName)
           
           
