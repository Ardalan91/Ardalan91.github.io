import json

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener
import requests
from os import environ

ENDPOINT = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"


class Listener(StreamListener):
    ENDPOINT = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
    TELEGRAM_BOT_API_KEY = ""
    TELEGRAM_CHANNEL_NAME = "@name" # @ symbol is mandatory
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        print(tweet)

        req = self.ENDPOINT.format(self.TELEGRAM_BOT_API_KEY,
                               self.TELEGRAM_CHANNEL_NAME,
                               tweet)
        requests.get(req)

        return True

def on_error(self, status):
        print ('error with status code' + str(status))

API_KEY= ""
API_SECRET = ""
ACCESS_TOKEN  = ""
ACCESS_TOKEN_SECRET = ""

auth = OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream = Stream(auth, Listener())
stream.filter(follow=["id"])

