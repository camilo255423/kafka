import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret_key = os.environ.get("CONSUMER_SECRET_KEY")


class StdOutListener(StreamListener):

    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        print("data", data)
        return True

    def on_error(self, status):
        print("status", status)


kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="trump")
