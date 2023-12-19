#pip install tweepy
#pip install textblob
#pip install matplotlib


import tweepy
import textblob
from textblob import TextBlob
import matplotlib.pyplot as plt
from datetime import datetime

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def analyze_sentiment(tweet):
    # Use TextBlob to perform sentiment analysis on the tweet text
    analysis = TextBlob(tweet)

    # Classify the polarity of the tweet (positive, neutral, negative)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

def plot_sentiment_over_time(timestamps, sentiments):
    # Plot sentiment over time
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, sentiments, marker='o', linestyle='-')
    plt.title('Sentiment Analysis Over Time')
    plt.xlabel('Time')
    plt.ylabel('Sentiment Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Input: Search query and the number of tweets to analyze
    search_query = input("Enter the search query: ")
    num_tweets = int(input("Enter the number of tweets to analyze: "))

    # Retrieve tweets based on the search query
    tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="en").items(num_tweets)

    # Analyze sentiment for each tweet and collect data for plotting
    timestamps = []
    sentiments = []

    for tweet in tweets:
        timestamp = datetime.strptime(str(tweet.created_at), "%Y-%m-%d %H:%M:%S")
        timestamps.append(timestamp)

        sentiment = analyze_sentiment(tweet.text)
        sentiments.append(sentiment)

        print(f'Tweet: {tweet.text}')
        print(f'Sentiment: {sentiment}\n')

    # Plot sentiment over time
    plot_sentiment_over_time(timestamps, sentiments)

if __name__ == "__main__":
    main()
