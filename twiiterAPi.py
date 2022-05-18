import pandas as pd 
from dateutil.relativedelta import relativedelta
import time
from ast import While
from pickle import TRUE
import tweepy
import csv
from datetime import datetime
from datetime import timedelta

from zmq import NULL
# your bearer token
MY_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABjUbgEAAAAAohIJZiYrWjPcBBwl9DiK7bSCL8w%3DRdQ7xs6H6g2swF8ensSP8FBIxifcWC4zrMLnucJPDdajAd86J5"
# create your client
client = tweepy.Client(bearer_token=MY_BEARER_TOKEN)

start_time = datetime.strptime("2022-05-12T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
end_time = datetime.strptime("2022-05-15T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")


def twitter_method(query, next_token):
    # # your start and end time for fetching tweets
    # minutes_to_add = 45
    # time_str = '12/05/2022 11:12:22.234513'
    # date_format_str = '%d/%m/%Y %H:%M:%S.%f'
    # # create datetime object from timestamp string
    # given_time = datetime.strptime(time_str, date_format_str)
    # print('Given timestamp: ', given_time)
    # n = 30
    # #Add 30 minutes to datetime object
    # final_time = given_time + relativedelta(minutes=n)
    # datetime_new = datetime_new + timedelta(minutes = minutes_to_add)


    # get tweets from the API
    if not next_token:

        tweets = client.search_recent_tweets(query=query,
                                            tweet_fields=[
                                                "created_at", "text", "source", "geo"],
                                            user_fields=[
                                                "name", "username", "location", "verified", "description", "entities", "id"],
                                            place_fields=["country"],
                                            max_results=100,
                                            expansions='author_id'
                                            )

    else:
        tweets = client.search_recent_tweets(query=query,
                                            next_token=["next_token"],
                                            tweet_fields=[
                                                "created_at", "id","text", "source", "geo"],
                                            user_fields=[
                                                "name", "username", "location", "verified", "description", "entities", "id"],
                                            place_fields=["country"],
                                            max_results=100,
                                            expansions='author_id'
                                            )

    # tweet specific info
    print(len(tweets.data))
    # user specific info
    print(len(tweets.includes["users"]))

    # first tweet
    first_tweet = tweets.data[0]
    dict(first_tweet)

    # import the pandas library

    # create a list of records
    tweet_info_ls = []

    # iterate over each tweet and corresponding user details
    for tweet, user in zip(tweets.data, tweets.includes['users']):
        tweet_info = {
            'created_at': tweet.created_at,
            'text': tweet.text,
            'source': tweet.source,
            'geo': tweet.geo,
            'id' : tweet.id,
            'name': user.name,
            'username': user.username,
            'location': user.location,
            'verified': user.verified,
            'description': user.description,
            "entities": user.entities,
            'country': user.location
        }
        tweet_info_ls.append(tweet_info)
    # create dataframe from the extracted records
    tweets_df = pd.DataFrame(tweet_info_ls)

    # save dataset
    tweets_df.to_csv('c:\\temp\\file2.csv', header=True, index=True, mode='a')
    print(tweets.meta)
    return tweets.meta["next_token"]


next_token = twitter_method("nba","")

while(True):
    next_token = twitter_method("nba","")
    
   # time.sleep(2100)