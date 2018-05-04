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
			for tweet in api.search(q=theTerm, lang='en', result_type='mixed', count=100, tweet_mode='extended', max_id=maxId)['statuses']:
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



consumer_key = '3tjpAl2B4uADbUdMQpaKcD6wB'
consumer_secret = 'vYXy8kJud07mScO7mDIEi3TyzQ6bFK48XbIUbuf4lftJkt1kB8'
access_token = '769581680-v9OUTVP5GAUm6C8DgxMidd3fa33FrZWvMPWpTpy3'
access_token_secret = 'LQYK9bxMk3VU4Lbdz6N1WeBMwpGY3TW0XWUn9Lpay8GYo'


api = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
	
collectTweets(sys.argv[1], sys.argv[2], api)



