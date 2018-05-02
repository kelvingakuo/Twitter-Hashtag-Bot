from twython import Twython
import sys
import csv
import json
import time


def collectTweets(searchTerm, filename, api, since=None, obj={}):
	theTerm = '#' + str(searchTerm) + '-filter:retweets AND -filter:replies'
	ids = []

	if(len(obj)==0):
		tweetObjects = {}
		tweetObjects['TweetData']=[]
	
	else:
		tweetObjects = obj
		tweetObjects['TweetData']=obj['TweetData']



	with open(filename, 'a') as dump:
		for tweet in api.search(q=theTerm, lang='en', result_type='mixed', count=100, tweet_mode='extended', since_id=since)['statuses']:
			ids.append(tweet['id'])
			tweetObjects['TweetData'].append(tweet)
			time.sleep(5)
		
		if(len(ids)==0):
			json.dump(tweetObjects, dump)
			print("Finished. {} tweets collected".format(len(tweetObjects['TweetData'])))
			return 
		else:
			sorte = sorted(ids)
			highest = sorte[0]
			collectTweets(searchTerm, filename, api, highest, tweetObjects)



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


api = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
	
collectTweets(sys.argv[1], sys.argv[2], api)



