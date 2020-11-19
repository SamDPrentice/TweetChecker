import urllib.request
from bs4 import BeautifulSoup

#check tweets


# take in a command line arg for twitter account
handle = 'TheTweetOfGod'

# build twitter link
url = 'https://www.twitter.com/' + handle
# get page info
html = urllib.request.urlopen(url)

# Soup the tweets from rest of it
soup = BeautifulSoup(html, features="html.parser")
text = soup.get_text()
print(text)
# print out 5 most recent tweets to stdout

# check again for new tweets in 10 min's and print any new ones

