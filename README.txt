TwitterChecker Notes:

Required Site Packages:
beautifulsoup4
lxml
requests

install these using (if python included in your path otherwise append python to the front e.g. python pip install "sitepackage"): 
pip install beautifulsoup4
pip install lxml
pip install requests

Running it:
Twitter checker uses sys.argv to get passed a twitter handle to command line (if this step is missed, it will still provide an input option)
for example (whilst in the command line with pwd as TwitterCheckers root directory)

python checker.py realDonaldTrump

will kick off the process and return the last 5 tweets from realDonaldTrump

Options:
--help will display a help menu similar to this readme
-curl followed by a url will post collected tweets inside the TwitterChecker object.
e.g.
python checker.py realDonaldTrump -curl https://www.somewheretopostto.com/curlhandler/

How:
Twitter checker uses urllib native library to scrape twitter page. Default headers cause twitter to block pythons path and return a failed result.
To get around this python updates the headers in the request before sending to twitter so that twitter returns a relative page for a different browser.
The returned responce is then parsed with the help of beautiful soup and lxml and just the tweet text is passed along to the collection.
Initial run will print 5 most recent tweets.
A schedule is then created to run every 10 minutes to repeat the process and display any updated tweets
New tweets are then added to the collection
The collection than can be output to json if the arguement to do so was provided and posted to a curl handler