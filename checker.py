import sys
import urllib.request
import sched
import time
import json
try:
    import bs4 as bs
    import requests
except SystemError:
    print('This module requires site packages "BeautifulSoup", "lxml" and "requests"')
    print('Install these by using the "pip install beaufitulsoup4" command')
    print('And')
    print('"pip install lxml"')
    print('And')
    print('"pip install requests"')

# Notes: Tweet Checker uses urllib, beautiful soup & lmxl site packages
# Author: Samuel Prentice
# Last Update: 23-11-2020

schedule = sched.scheduler(time.time, time.sleep)


class TweetChecker:
    handle = ''
    url = 'https://www.twitter.com/'
    collection = []
    made_first_request = False

    def __init__(self, *args):
        # Check args provided
        if len(args[0]) < 2:
            print('checker.py takes 1 additional argument, you provided', str(len(sys.argv)))
        elif '--help' in args[0]:
            print('TwitterChecker <twitter handle> <option> <option url>')
            print()
            print('To just print out latest tweets, just enter a user handle without the @ symbol')
            print('Most recent tweets will be updated every 10 minutes')
            print('To use the curl option enter "user_handle -curl website_to_post_to"')
        elif len(args[0]) == 2:
            self.handle = args[0][1]
        elif len(args[0]) == 4:
            if '-curl' == args[0][2]:
                self.handle = args[0][1]
                self.run_all()
                self.post_curl(args[0][3])

    def run_all(self):
        self.make_request()
        self.make_soup()
        self.print_last_five()

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

    def post_curl(self, url):
        payload = self.get_json()
        requests.post(url, data=payload)

    def get_json(self):
        return json.dumps(self.__dict__)


def update_every_ten_minutes(checker):
    checker.run_all()
    schedule.enter(600, 1, update_every_ten_minutes, (checker,))
    schedule.run()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        tc = TweetChecker(sys.argv)
        update_every_ten_minutes(tc)
    else:
        # Option to enter it later if missed in original args
        print('Welcome to TwitterChecker')
        handle = input('Enter twitter handle:')
        tc = TweetChecker(['checker.py', handle])
        update_every_ten_minutes(tc)
