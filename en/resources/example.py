import tweepy
import json

with open('/home/mjs/twitterauth.json') as file:
    secrets = json.load(file)

auth = tweepy.OAuthHandler(secrets['Consumer_Key'], secrets['Consumer_Secret'])
auth.set_access_token(secrets['Access_Token'], secrets['Access_Token_Secret'])

twitter = tweepy.API(auth)

twitter.update_with_media('cat.png', 'The Internet needs more cats.')
