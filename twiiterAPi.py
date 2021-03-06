import json
from msilib.schema import SelfReg
from numpy import place
import pandas as pd
from dateutil.relativedelta import relativedelta
import time
from ast import While
from pickle import TRUE
import tweepy
from datetime import datetime
from datetime import timedelta

from twitter_authentication import bearer_token

def twitter_method(query, next_token):
    # get tweets from the API
    if not next_token:

        tweets = client.search_recent_tweets(query=query,
                                             tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
                                             user_fields=[
                                                 'created_at','description','entities','id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],
                                             place_fields=['contained_within','country','country_code','full_name','geo','id','name','place_type'],
                                             max_results=100,
                                             media_fields= ['alt_text','duration_ms','height','media_key','non_public_metrics','organic_metrics','preview_image_url','promoted_metrics','public_metrics','type','url','variants','width'],
                                             expansions=['author_id','attachments.media_keys','geo.place_id']
                                             )

    else:
        tweets = client.search_recent_tweets(query=query,
                                             next_token=["next_token"],
                                             tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
                                             user_fields=[
                                                 'created_at','description','entities','id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],
                                             place_fields=['contained_within','country','country_code','full_name','geo','id','name','place_type'],
                                             max_results=100,
                                             media_fields= ['alt_text','duration_ms','height','media_key','non_public_metrics','organic_metrics','preview_image_url','promoted_metrics','public_metrics','type','url','variants','width'],
                                             expansions=['author_id','attachments.media_keys','geo.place_id']
                                             )

    


    tweet_info_ls = []
    tweets_df = pd.DataFrame(tweet_info_ls)
    

    for tweet, user in (t for t in zip(tweets.data, tweets.includes['users']) if t[0].lang == 'en'):
        tweet_info = {
            'attachments': tweet.attachments,
            'lang' : tweet.lang,
            'author_id': tweet.author_id,
            'created_at':	tweet.created_at,
            'mentions':	None if tweet.entities is None else [o.get('username') for o in tweet.get('entities',{}).get('mentions',[])],
            'hashtags':	None if tweet.entities is None else [o.get('tag') for o in tweet.get('entities',{}).get('hashtags',[])],
            'geo':	tweet.geo,
            'id':	tweet.id,
            'source':	tweet.source,
            'text':	tweet.text,
            'name': user.name,
            'retweet_count': tweet.get('public_metrics',{}).get('retweet_count',[]),
            'like_count': tweet.get('public_metrics',{}).get('like_count',[]),
            'user_followers_count':user.get('public_metrics',{}).get('followers_count',[]),
            'user_following_count':user.get('public_metrics',{}).get('following_count',[]),
            'tweet_user_count':user.get('public_metrics',{}).get('tweet_count',[]),
            'user_id': user.id,
            'username': user.username,
            'location': user.location,
            'verified': user.verified,
            'description': user.description,
            "entities": user.entities,
            'country': user.location,
            'tweet_context_annotations': None if tweet.context_annotations is None else [o.get('domain') for o in tweet.get('context_annotations',{})]
            
        }
        tweet_info_ls.append(tweet_info)

    # save dataset
    
    for tweet in tweet_info_ls:
                with open("results.json", "a" ) as f:
                    f.write(json.dumps(tweet, indent=4, sort_keys=True, default=str) + "\n")
    return tweets.meta["next_token"]

# your bearer token
MY_BEARER_TOKEN = bearer_token
# create your client
client = tweepy.Client(bearer_token=MY_BEARER_TOKEN)

next_token = twitter_method("ChampionsLeague final", "")

while(True):
    next_token = twitter_method("ChampionsLeague final", "")

    time.sleep(300)
