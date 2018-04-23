from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib2
import time
import csv
import sys

def scrollToBottom():
	lastHeight = driver.execute_script('return document.body.scrollHeight')
	while True:
		driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
		time.sleep(15)

		newHeight = driver.execute_script('return document.body.scrollHeight')
		if newHeight == lastHeight:
			break
		lastHeight = newHeight

def returnURL(term):  # term is hasthag to search
	return 'https://twitter.com/hashtag/{}?src=hash'.format(term)

def scrapePage(driver, theSearch):
	time.sleep(5)

	tweets = driver.find_elements_by_xpath('//li[@data-item-type="tweet"]')

	with open(theSearch+'.csv','a') as dump:
		writer = csv.writer(dump)
		for tweet in tweets:
			username = tweet.find_element_by_class_name('username').find_element_by_tag_name('b').text.encode('ascii','ignore').decode('ascii')
			username = '@'+username
			text = tweet.find_element_by_class_name('js-tweet-text').text.encode('ascii','ignore').decode('ascii')
			theDate = tweet.find_element_by_class_name('time').find_element_by_tag_name('a').text.encode('ascii','ignore').decode('ascii')
#_by_xpath('//small[@class="time"]')
			footerObject = tweet.find_element_by_class_name('stream-item-footer')


			retweets = footerObject.find_element_by_css_selector('.ProfileTweet-action.ProfileTweet-action--retweet.js-toggleState.js-toggleRt').find_element_by_class_name('ProfileTweet-actionCountForPresentation').text.encode("ascii","ignore").decode("ascii")
			likes = footerObject.find_element_by_css_selector('.ProfileTweet-action.ProfileTweet-action--favorite.js-toggleState').find_element_by_class_name('ProfileTweet-actionCountForPresentation').text.encode("ascii","ignore").decode("ascii")
			replies = footerObject.find_element_by_css_selector('.ProfileTweet-action.ProfileTweet-action--reply').find_element_by_class_name('ProfileTweet-actionCountForPresentation').text.encode("ascii","ignore").decode("ascii")

			writer.writerow([username, text, theDate, retweets, likes, replies])





path = 'path/to/Selenium/webdriver.exe'
driver = webdriver.Chrome(path)


searchTerm = sys.argv[1]
url = returnURL(searchTerm)
driver.get(url)
driver.maximize_window()
scrollToBottom()
scrapePage(driver, searchTerm)
driver.quit()



