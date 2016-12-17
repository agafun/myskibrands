from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import os
from database import *

#Variables that contains the user credentials to access Twitter API
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']


class StdOutListener(StreamListener):

    def remove_characters(self, s, characters):
        result = s
        for character in characters:
            result = result.replace(character, '')
        return result

    def tweet_contains_words(self, tweet, words):
        tweeli = list(tweet.split())
        for item in words:
            if item in tweeli:
                return True
        return False

    def tweet_is_valid(self, text):
        ski_words = ['ski', 'skis', 'skiing']

        tweet1 = text.lower()
        tweet1 = self.remove_characters(tweet1, "!$%^&*_-+={}[]|:;<,>.?/")
        return self.tweet_contains_words(tweet1, ski_words)

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            tweet_id = tweet['id']
            tweet_text = tweet['text']
            tweet_favorite_count = tweet['favorite_count']
            tweet_lang = tweet['lang']
            tweet_place = tweet['place']
            tweet_timestamp_ms = float(tweet['timestamp_ms']) / 1000.0
            tweet_created_at = tweet['created_at']

            user = tweet['user']
            user_id = user['id']
            user_screen_name = user['screen_name']
            user_location = user['location']
            user_followers_count = user['followers_count']
            user_friends_count = user['friends_count']
            user_favourites_count = user['favourites_count']
            user_statuses_count = user['statuses_count']
            user_utc_offset = user['utc_offset']

            entities = tweet['entities']
            entities_hashtags = entities['hashtags']
            entities_user_mentions = entities['user_mentions']


            if self.tweet_is_valid(tweet_text):
                t = None
                u = User.create_or_get(id=user_id, screen_name=user_screen_name, location=user_location, followers_count=user_followers_count, friends_count=user_friends_count, favourites_count=user_favourites_count, statuses_count=user_statuses_count, utc_offset=user_utc_offset)
                place = ''
                if isinstance(tweet_place, dict):
                    place = tweet_place['name']
                try:
                    t = Tweet.create(id=tweet_id, user=u[0], text=tweet_text, favorite_count=tweet_favorite_count, lang=tweet_lang, place=place, timestamp_ms=tweet_timestamp_ms, created_at=tweet_created_at)
                except:
                    pass

                try:
                    for h in entities_hashtags:
                        Hashtag.create(hashtag=h['text'], tweet=t)
                except:
                    pass

                try:
                    for um in entities_user_mentions:
                        UserMention.create(screen_name=um['screen_name'], tweet=t)
                except:
                    pass

            return True
        except KeyError as e:
            print 'error: ', e

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['atomicski', 'atomicskis', 'atomic_ski', 'atomic_skis', 'weareskiing', 'blizzardski', 'blizzardskis', 'blizzard_ski', 'blizzard_skis', 'dynastarski', 'dynastarskis', 'dynastar_ski', 'dynastar_skis', 'weliveskiing', 'elanski', 'elanskis', 'elan_ski', 'elan_skis', 'elanskisales', 'fischerski', 'fischerskis', 'fischer_ski', 'fischer_skis', 'headski', 'headskis', 'head_ski', 'head_skis', 'headrebels', 'worldcuprebels', 'headwhatsyourlimit', 'k2ski', 'k2skis', 'k2_ski', 'k2_skis', 'k2skisuk', 'seriousfun', 'kaestle', 'kaestleski', 'kaestleskis', 'kaestle_ski', 'kaestle_skis', 'forskiers', 'kneissl', 'kneisslski', 'kneisslskis', 'kneissl_ski', 'kneissl_skis', 'kneissl_uk', 'nordicaski', 'nordicaskis', 'nordica_ski', 'nordica_skis', 'nordicausa', 'fitforthelongrun', 'rossignol', 'rossignolski', 'rossignolskis', 'rossignol_ski', 'rossignol_skis', 'rossignol_1907', 'anotherbestday', 'salomonski', 'salomonskis', 'salomon_ski', 'salomon_skis', 'salomonsports', 'timetoplay', 'salomontv', 'salomonnordic', 'stoeckli', 'stoeckliski', 'stoeckliskis', 'stoeckli_ski', 'stoeckli_skis', 'stoeckliracing', 'voelkl', 'voelklski', 'voelklskis', 'voelkl_ski', 'voelkl_skis', 'volklski', 'volklskis', 'volkl_ski', 'volkl_skis', 'simplyvolkl', 'atomic', 'blizzard', 'dynastar', 'elan', 'fischer', 'head', 'k2', 'nordica', 'salomon'])