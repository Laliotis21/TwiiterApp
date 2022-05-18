import tweepy


bearer_token = "AAAAAAAAAAAAAAAAAAAAABjUbgEAAAAAohIJZiYrWjPcBBwl9DiK7bSCL8w%3DRdQ7xs6H6g2swF8ensSP8FBIxifcWC4zrMLnucJPDdajAd86J5"

client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets(query='nba')
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)
print(response.data)
# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data
#for tweet in tweepy.Cursor(.userapi_timeline, screen_name='predictivehacks', tweet_mode="extended").items():
    #text = tweet._json["full_text"]
    #print(text)
# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)
    print(tweet.geo)
    #print(tweet.include.refreferenced_tweetserenc[0].id)
    #print(tweets)
    type(tweet)

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
response = client.search_recent_tweets("Tweepy", max_results=10)