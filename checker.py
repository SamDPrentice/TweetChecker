import sys
import urllib.request
try:
    import bs4 as bs
except SystemError:
    print('This module requires site packages "BeautifulSoup" and "lxml"')
    print('Install these by using the "pip install beaufitulsoup4" command')
    print('And')
    print('"pip install lxml"')

# Notes: Tweet Checker uses urllib, beautiful soup & lmxl site packages
# Author: Samuel Prentice
# Last Update: 23-11-2020


class TweetChecker:
    handle = ''
    url = 'https://www.twitter.com/'
    collection = []
    made_first_request = False

    def __init__(self, *args):
        if len(args[0]) != 2:
            print('checker.py takes 1 additional argument, you provided', str(len(sys.argv)))
            print(str(args))
            print(str(len(args)))
        else:
            self.handle = args[0][1]
            self.make_request()
            self.make_soup()

    def make_request(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) '
                                 'Chrome/24.0.1312.27 Safari/537.17'}
        request = urllib.request.Request(self.url + self.handle, headers=headers)
        return request

    def make_soup(self):
        response = urllib.request.urlopen(self.make_request())
        soup = bs.BeautifulSoup(response, 'lxml')
        tweets = soup.find_all('div', {"class": "tweet-text"})
        for tweet in tweets:
            if tweet.text not in self.collection:
                if self.made_first_request:
                    self.collection.insert(0, tweet.text)
                else:
                    self.collection.append(tweet.text)
        self.made_first_request = True

    def print_last_five(self):
        for tweet in range(0, 5):
            print(self.collection[tweet])


if __name__ == '__main__':
    tc = TweetChecker(sys.argv)
    tc.print_last_five()
