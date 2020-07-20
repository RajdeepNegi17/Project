4. Twitter Sentiment Analysis using Python


Introduction:
Sentiment Analysis is the process of computationally determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.


Problem Statement:
We have to distinguish whether the sentiments of a tweet is positive, negative or neutral and finding the percentage of positive or negative tweets.


Procedure:
We will be fetching tweets through the TwitterAPI.For that purpose we have to first register one app through our twitter account.And then after doing it, we will be allocated api key,api secret key,access token,access token secret . These all will be different for different users and are senitive like passwords therfore in the code I have replaced them with some random numbers. Anyone can write their personal api_key or secret_key in the code and then can access the tweets from the TwitterAPI.

After getting those keys, we will start by importing some important libraries like tweepy,textblob,etc. Then we will create one class where first of all we will initialise the keys and token.Inside that class we will write several functions . Before it we will make a GET request to Twitter API to fetch tweets for a particular query.

We made a get_tweets function which will fetch tweets and parse them.

We also have a get_tweet_sentiment function to classify sentiment of passed tweet using textblob's sentiment method which will be using textblob library.

We have one clean_tweet function to clean tweet text by removing links, special characters using simple regex statements. 

We Passed the tokens to the sentiment classifier which classifies the tweet sentiment as positive, negative or neutral by assigning it a polarity between -1.0 to 1.0. 

After doing all this we can pass any person's name, or about any trending place,player,topic etc. in the query and we will get the tweets about them in the output as well as the percentage of the positive tweets and negative tweets about that person or topic/place that people are tweeting in the twitter.

Conclusion:
We have made a twitter sentiment analyser using python that tells us about the positive or negative tweets about a specific topic or person/place/thing that are being tweeted in the Twitter.