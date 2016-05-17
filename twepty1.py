import json
#import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sentmod as s
import codecs
ckey='U59lRzdTsh3dmGuVxA7PS3DAw'
csecret='tkbjVStD8nWC0q4d5yWUGWZukRMgTAL4NR0F4ePFYVI4mutR0H'
atoken='3559529532-KABX6bfcbvVbWUfsf3shoMxfUweLMg3WNm4SKPo'
asecret='ZeucCbFFNPrTvocY8gF0TtBdGWRr9sd7it8J6LaVk7Je9'



class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)
		tweets = all_data["text"]
		sentiment_value,confidence = s.sentiment(tweets)
		print tweets,sentiment_value,confidence
		if confidence*100>=80:
		  	output = open("twittersent.txt","a")
                 #output.write(tweets)
		 # output.write("::::")
		  	output.write(sentiment_value)
		  	output.write("\n")
                  	output.close()
		return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
