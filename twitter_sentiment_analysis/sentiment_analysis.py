import tweepy
from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import pprint

consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 

def sentimental_analysis():
	
	search_for=input('Enter the term/hastag')
	
	noOfterms=int(input('Number of tweets'))
	
	tweets=tweepy.Cursor(api.search,q=search_for,lang='English').items(noOfterms)
	
	positive=0
	negative=0
	neutral=0
	polarity=0

	for tweet in tweets:
		analysis=TextBlob(tweet.text)
		polarity+=analysis.sentiment.polarity

		if analysis.sentiment.polarity==0:
			neutral+=1
		elif analysis.sentiment.polarity>0.00:
			positive+=1
		elif analysis.sentiment.polarity<0.00:
			negative+=1	

	labels = 'Positive', 'Negative', 'Neutral'
	sizes = [positive,negative, neutral]
	colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
	explode = (0.1, 0, 0)  
	 
	
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	        autopct='%1.1f%%', shadow=True, startangle=140)
	 
	plt.axis('equal')
	plt.show()


if __name__=='__main__':
    sentimental_analysis()
  
  
  
  
