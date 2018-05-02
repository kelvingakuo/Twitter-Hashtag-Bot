from twython import Twython
import sys
import csv
import json


def collectTweets(searchTerm, filename, api):
	searchTerm = '#' + str(searchTerm)
	tweetObjects = {}
	tweetObjects['TweetData']=[]

	with open(filename, 'a') as dump:
		for tweet in api.search(q=searchTerm, lang='en', result_type='recent', count=100, tweet_mode='extended')['statuses']:
			tweetObjects['TweetData'].append(tweet)
		json.dump(tweetObjects, dump)


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


api = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
	
collectTweets(sys.argv[1], sys.argv[2], api)


