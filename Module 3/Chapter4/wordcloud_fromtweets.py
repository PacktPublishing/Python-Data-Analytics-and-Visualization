import tweepy
import json
import sys
import codecs

counter = 0
MAX_TWEETS = 500

#Variables that contains the user credentials to access Twitter API 
#Google search how to get the authentication keys 
access_token = "Access Token"
access_token_secret = "Access Secret"
consumer_key = "Consumer Key"
consumer_secret = "Consumer Secret"

fp = codecs.open("filtered_tweets.txt", "w", "utf-8")

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        global counter
        fp.write(status.text)
        print "Tweet-count:" +str(counter)
        counter += 1
        if counter >= MAX_TWEETS: sys.exit()

    def on_error(self, status):
        print status

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    streaming_api = tweepy.streaming.Stream(auth,
               CustomStreamListener(), timeout=60)

    streaming_api.filter(track=['python program', 'statistics', 
             'data visualization', 'big data', 'machine learning'])

