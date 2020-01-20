#! python3
# Automate Boring Stuff Practice Project - Chapter 11
# linkVerif.py - Downloads and verifies all the links in a given webpage

import requests, bs4, pprint

# Gets all the links from a given url
def getLinks(theURL):
    # This header is a standard Firefox webbrowser header, it helps with preventing the
    # website from identifying the scrip as an automatic scraping code and retunrning unusable
    # responses    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    # The list of element containing links
    searchElems = ['href', 'src']
    
    # Send requests to server
    r = requests.get(theURL, headers=headers)
    r.raise_for_status()

    # Create the SOAP object
    s = bs4.BeautifulSoup(r.text, features='lxml')

    # Create a list and append every link that meets the criteria set in searchElems list
    l = []
    for elem in searchElems:
        linkElem = s.select('body ['+elem+']')
        # for links in linkElem:
        #     l.append(links.get(elem))
        l += [links.get(elem) for links in linkElem]  # this line replaces the 
                              # two lines above, this is a "list comprehension"
    return l

# Tests all the links provided in a list
def testLinks(theLinks):
    # This header is a standard Firefox webbrowser header, it helps with preventing the
    # website from identifying the scrip as an automatic scraping code and retunrning unusable
    # responses
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    # Create a dictionary with each link having a valid/invalid value accordingly
    verLinks = {}

    # Check if the links start with http, add if needed
    for links in theLinks:
        if 'http' not in links:
            links = 'https:'+ links
        # Try the link by sending a request to the server with the link as url
        try:
            r = requests.get(links, headers=headers)
            r.raise_for_status()
        # If error then assing the value of invalid to the link in the dictionary
        except:
            verLinks.setdefault(links, 'invalid')
        verLinks.setdefault(links, 'valid')
    return verLinks                
                
  
        
url = 'https://www.flickr.com/search/?text=parrot'
##url = 'https://imgur.com/search?q=parrots'
pprint.pprint(testLinks(getLinks(url)))
