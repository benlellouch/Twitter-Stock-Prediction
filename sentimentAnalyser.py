import re
import tweepy
from tweepy import OAuthHandler
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class TwitterFetcher:

    def __init__(self):

        consumer_key = open("consumerkey.txt", "r").readline().rstrip()
        consumer_secret = open ("consumersecret.txt", "r").readline().rstrip()
        access_token = open ("accesstoken.txt", "r").readline().rstrip()
        access_token_secret = open ("accesstokensecret.txt", "r").readline().rstrip()

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())

    def get_tweets(self, query, count):
        tweets = []

        try:
            fetched_tweets = self.api.search(q = query, count = count, lang = "en")

            for tweet in fetched_tweets:
                parsed_tweet = (self.clean_tweet(tweet.text) , tweet.created_at)


                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            print ("Error : " + str(e) )

class SentimentAnalyser:

    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def analyse(self, tweets):

        analysed_tweets = []

        for tweet in tweets:

            compound_score = self.sid.polarity_scores(tweet[0])['compound']
            analysed_tweet = (compound_score, tweet[1])

            if(compound_score != 0.0):
                analysed_tweets.append(analysed_tweet)



        return analysed_tweets

    def average_score(self, analysed_tweets):

        cumsum = 0
        for tweet in analysed_tweets:
            cumsum += tweet[0]
        return (cumsum/len(analysed_tweets))
