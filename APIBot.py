from twython import Twython
import sys
import csv
import json
import time


def collectTweets(searchTerm, filename, api, maxId=None, obj={}):
	theTerm = '#' + str(searchTerm) + '-filter:retweets AND -filter:replies'
	ids = []

	if(len(obj)==0):
		tweetObjects = {}
		tweetObjects['TweetData']=[]
	
	else:
		tweetObjects = obj
		tweetObjects['TweetData']=obj['TweetData']



	with open(filename, 'a') as dump:
		try:
			for tweet in api.search(q=theTerm, lang='en', result_type='recent', count=100, tweet_mode='extended', max_id=maxId)['statuses']:
				ids.append(tweet['id'])
				tweetObjects['TweetData'].append(tweet)
			
			if(len(ids)==0):
				json.dump(tweetObjects, dump)
				print("Finished. {} tweets collected".format(len(tweetObjects['TweetData'])))
				return 
			else:
				sorte = sorted(ids)
				highest = sorte[0]-1
				collectTweets(searchTerm, filename, api, highest, tweetObjects)
		except TwythonError as e:
			print(e.error)



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


api = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
	
collectTweets(sys.argv[1], sys.argv[2], api)



