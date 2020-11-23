import sys
import urllib.request
import bs4 as bs

# check tweets

# grab args
if len(sys.argv) != 2:
    print('checker.py takes 1 additional argument, you provided', str(len(sys.argv)))
else:
    # take in a command line arg for twitter account
    handle = sys.argv[1]

# build twitter link
url = 'https://www.twitter.com/' + handle

# get page info
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

# Soup the tweets from rest of it
soup = bs.BeautifulSoup(response, 'lxml')
tweets = soup.find_all('div', {"class": "tweet-text"})
#tweet_dates = soup.find_all('time')

# print out 5 most recent tweets to stdout
print('Printing 5 most recent tweets for @' + handle)
for t in range(0, 5):
#    print(tweet_dates[t].text)
    print(tweets[t].text)

#for t in tweet_dates:
#    print(t)

# check again for new tweets in 10 min's and print any new ones



