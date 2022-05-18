
import tweepy
import sys
import csv
import re

CONSUMER_KEY='LnOk1bifetyFwQ3o1CNSoKSCE'
CONSUMER_SECRET='NiZMECFpACmf6FnhBt6NsoshibtKzIxQXAq3DdiYm1HnKS6ljh'
ACCESS_TOKEN='238717829-oWfInA4sbq2fBVZoQvxQ14oWOl7KIUkhvvR0NYq3'
ACCESS_TOKEN_SECRET='BovwdpnVmtROIXoRecsvQOGyspi399jaHZ2RmVycnLFcf'

"""https://stackoverflow.com/a/49986645/3711660"""
def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


# 1. Authenticate
auth = tweepy.OAuthHandler(CONSUMER_KEY,   CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

if (not api):
    print("Authentication failed!")
    sys.exit(-1)

# 2. Get data
data = api.search_tweets("elonmusk", tweet_mode="extended",
                         count=10, exclude_replies=True)
#tweepy.models.Statustweepy.models.Status


for tweet in tweepy.Cursor(api.search_tweets, q="#BTC", count=10, tweet_mode='extended').items():
    tweet._json["created_at"]
    tweet._json['retweet_count']
    tweet._json['favorite_count']
# 3. Save data
with open('elon_tweets.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['created_at', 'text', 'geo', 'profile_image_url_https' 'lang', 'retweet_count','display_url','profile_use_background_image','screen_name']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()

    for tweetObject in data:
        writer.writerow({'text': deEmojify(tweetObject.full_text),
                         'created_at': tweetObject.created_at})

print('DONE!')