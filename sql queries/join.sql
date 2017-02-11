select * from hashtag
inner join tweet 
on hashtag.tweet_id = tweet.id
inner join skibrands
on hashtag.hashtag like skibrands.hashtag