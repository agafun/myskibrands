select distinct tweet.id, user_id, text, favorite_count, lang, place, timestamp_ms, brand, location, followers_count, utc_offset from tweet
inner join skibrands
on tweet.text like '%'||skibrands.hashtag||'%'
inner join user
on tweet.user_id = user.id
where text like "%ski%";