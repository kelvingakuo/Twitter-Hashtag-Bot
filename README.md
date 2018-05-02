A Twitter bot to extract tweets of a given hashtag<br>

<b>SETUP </b><br>
a. <code>pip install selenium</code><br>
b. <code>pip install twython</code><br>


<b>USAGE </b><br>\
<b>Note: Both bots only retrieve tweets associated with a hashtag. Pass the search term without '#' to the terminal</b><br><br>
1. To extract tweets for hashtags older than a week old(Web crawling) <br>
	a) Download Selenium Webdriver for Chrome. Change path accordingly on line 49 of crawlerBot.py<br>
	b) <code>python crawlerBot.py hashtagToSearch filename.csv</code> 
	c) On a CSV file with the passed name, for every tweet, the following are saved:<br>
     	i. Username <br>
     	ii. The tweet <br>
     	iii. The date <br>
     	iv. Number of retweets <br>
     	v. Number of likes<br>
     	vi. Number of replies<br><br>


2. To extract tweets for hashtags less than a week old (Using Twitter API)<br>
	a) Go to https://apps.twitter.com/ and register for API keys. Update lines 39-42 appropriately<br>
	b) <code>python APIBot.py hashtagToSearch filename.json</code> 
	c) On a JSON file with the passed name, ALL the data provided for each tweet(IT'S A LOT!!) by the Twitter API is dumped as as a JSON array 

    
   
