import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret_key = os.environ.get("CONSUMER_SECRET_KEY")
