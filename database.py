from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('tweets.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = BigIntegerField(primary_key=True)
    screen_name = CharField()
    location = CharField(null=True)
    followers_count = IntegerField()
    friends_count = IntegerField()
    favourites_count = IntegerField()
    statuses_count = IntegerField()
    utc_offset = IntegerField(null=True)

class Tweet(BaseModel):
    id = BigIntegerField(primary_key=True)
    user = ForeignKeyField(User, related_name='tweets')
    text = TextField()
    favorite_count = IntegerField()
    lang = CharField()
    place = CharField(null=True)
    timestamp_ms = TimestampField()
    created_at = TextField()

class TweetOriginal(BaseModel):
    tweet = ForeignKeyField(Tweet, related_name='tweetorigin')
    tweet_json = CharField()
    
class Hashtag(BaseModel):
    hashtag = CharField()
    tweet = ForeignKeyField(Tweet, related_name='hashtags')

class UserMention(BaseModel):
    screen_name = CharField()
    tweet = ForeignKeyField(Tweet, related_name='user_mentions')

db.connect()
db.create_tables([User, Tweet, Hashtag, UserMention], safe=True)
