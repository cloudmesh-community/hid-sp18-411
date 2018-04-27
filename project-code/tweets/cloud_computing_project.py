import tweepy
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re
import html
from textblob import TextBlob
import matplotlib.pyplot as plt

# Removed API Key and Secret
def twitter_download(hashtag):
    API_KEY = ''
    API_SECRET = ''
    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    c = tweepy.Cursor(api.search, q=hashtag, lang="en")

    tweet_store = []
    for status in c.items(100):
        tweet_store.append(status.text)

    df = pd.DataFrame({'tweets': tweet_store})

    # Saving the data to a csv file
    df.to_csv('./usr/local/static/tweet_cloud_me.csv', sep=',', encoding='utf-8', index=False)

    # Pre-Processing the tweets data from twitter
    tweets_url_removed = []
    tweets_mentions_removed = []
    tweets_clean = []

    df1 = df.copy()

    # Removing HTML Characters
    tweet = html.unescape(df1)

    # Reading the dataframe of tweets into a list structure
    tweets = tweet['tweets'].values.tolist()
    del tweet

    # Removing URLS from the tweets
    for i in range(len(tweets)):
        tweets_url_removed.append(re.sub(r'http\S+', '', tweets[i]))

    # Removing the mentions (eg:- @someone) from the tweets
    for i in range(len(tweets_url_removed)):
        tweets_mentions_removed.append(
            ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweets_url_removed[i]).split()))

    # Removing the stop words from the tweets
    for i in range(len(tweets_mentions_removed)):
        tweets_clean.append(
            ' '.join([word for word in tweets_mentions_removed[i].split() if word not in (stopwords.words('english'))]))

    del tweets_mentions_removed, tweets_url_removed
    # Converting the cleaned tweets data to a dataframe

    tweets_df = pd.DataFrame({'tweets': tweets_clean})

    # Removing the empty entries after Pre-Processing
    tweets_df['tweets'].replace('', np.nan, inplace=True)
    tweets_df.dropna(subset=['tweets'], inplace=True)

    tweets_clean = tweets_df.values.tolist()

    # Saving the clean data to a csv file
    tweets_df.to_csv('./usr/local/static/tweet_clean.csv', sep=',', encoding='utf-8', index=False)

    # Determining the Sentiment of the Tweet
    scores = []
    polarity = []

    for i in range(int(len(tweets_clean))):
        text = TextBlob(str(tweets_clean[i]))
        scores.append(format(text.sentiment.polarity, '.2f'))

    for i in range(len(scores)):
        if float(scores[i]) == 0.00:
            polarity.append(0)
        elif float(scores[i]) < 0.00:
            polarity.append(2)
        elif float(scores[i]) > 0.00:
            polarity.append(1)

    final_df = pd.DataFrame({'Tweets': tweets_clean, 'Sentiment': polarity})

    # Saving the results to a csv file
    final_df.to_csv('./usr/local/static/tweet_sentiment.csv', sep=',', encoding='utf-8', index=False)
