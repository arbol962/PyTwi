#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Tweepyライブラリをインポート
import tweepy

#各種キーをセット
CONSUMER_KEY = '2g0oC8mdtEDAx5xSpkA4HDZv2'
CONSUMER_SELECT = 'qTII7GXNYWuNwLInHARmRwzjF4iMPW5iHgxcTUXBMRTztTfD4s'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SELECT)
ACCESS_TOKEN = '728159306-BCwLVM4rUzlNbHVMZ9BKjoNzsRCOx8dhnRFePTl1'
ACCESS_SECRET = 'wYwKU1DTwXLplEnabGKyRmSkwjV1l6RujPGx16CT1SlJG'
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

#CREATE API INSTANCE
api = tweepy.API(auth)

print("Done!")
