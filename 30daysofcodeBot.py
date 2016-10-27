import tweepy
from time import sleep
from secrets import *

# log into the twitter account 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_secret)
auth.secure = True
api= tweepy.API(auth)

mybot = api.get_user(screen_name="@30daysofcode")

# code for bot
for tweet in tweepy.Cursor(api.search, q='30daysofcode', lang= 'en').items(100):
	try:
		if tweet.user.id == mybot.id:
			continue

		print "\n\n Found tweet by: @" + tweet.user.screen_name
		if (tweet.retweeted == False) or (tweet.favorited == False):
			tweet.retweet()
			tweet.favorite()
			#print "retweeted and favorited"
		if tweet.user.following == False:
			tweet.user.follow()
			#print "followed the user"

	except tweepy.TweepError as e:
		#print e.reason
		sleep(10)
		continue

	except StopIteration:
		break
