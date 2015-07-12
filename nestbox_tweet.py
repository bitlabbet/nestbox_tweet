#!/usr/bin/env python

import tweepy
from tweepy import OAuthHandler

api_key = 'YOURAPIKEY'
api_secret = 'YOURAPISECRET'
access_token = 'YOURACCESSTOKEN'
token_secret = 'YOURTOKENSECRET'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth)
my_twitter = api.me()
api.update_with_media('/path/to/your/image.jpg')
