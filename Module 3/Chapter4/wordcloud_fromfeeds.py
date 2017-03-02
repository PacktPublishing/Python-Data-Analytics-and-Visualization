import feedparser
from os import path
import re

d = path.dirname(__file__)
mystopwords = ['test', 'quot', 'nbsp']

feedlist = ['http://www.techcrunch.com/rssfeeds/',
'http://www.computerweekly.com/rss',
'http://feeds.twit.tv/tnt.xml',
'https://www.apple.com/pr/feeds/pr.rss',
'https://news.google.com/?output=rss'
'http://www.forbes.com/technology/feed/'                  'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',         'http://www.nytimes.com/roomfordebate/topics/technology.rss',
'http://feeds.webservice.techradar.com/us/rss/reviews'            'http://feeds.webservice.techradar.com/us/rss/news/software',
'http://feeds.webservice.techradar.com/us/rss',
'http://www.cnet.com/rss/',
'http://feeds.feedburner.com/ibm-big-data-hub?format=xml',
'http://feeds.feedburner.com/ResearchDiscussions-DataScienceCentral?format=xml',        'http://feeds.feedburner.com/BdnDailyPressReleasesDiscussions-BigDataNews?format=xml',
'http://http://feeds.feedburner.com/ibm-big-data-hub-galleries?format=xml',          'http://http://feeds.feedburner.com/PlanetBigData?format=xml',
'http://rss.cnn.com/rss/cnn_tech.rss',
'http://news.yahoo.com/rss/tech',
'http://slashdot.org/slashdot.rdf',
'http://bbc.com/news/technology/']          

def extractPlainText(ht):
    plaintxt=''
    s=0
    for char in ht:
        if char == '<': s = 1
        elif char == '>': 
            s = 0
            plaintxt += ' '
        elif s == 0: plaintxt += char
    return plaintxt
    
def separatewords(text):
    splitter = re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s) > 3]
    
def combineWordsFromFeed(filename):
    with open(filename, 'w') as wfile:
      for feed in feedlist:
        print "Parsing " + feed
        fp = feedparser.parse(feed)
        for e in fp.entries:
          txt = e.title.encode('utf8') + \
               extractPlainText(e.description.encode('utf8'))
          words = separatewords(txt)
          
          for word in words:
            if word.isdigit() == False and word not in mystopwords:
               wfile.write(word)
               wfile.write(" ")
          wfile.write("\n")
    wfile.close()
    return

combineWordsFromFeed("wordcloudInput_FromFeeds.txt")

