def remove_characters(s, characters):
    result = s
    for character in characters:
        result = result.replace(character, '')
    return result

def tweet_contains_words(tweet, words):
    tweeli = list(tweet.split())
    for item in ski_words:
        if item in tweeli:
            #print 'Valid', item
            return True
    return False


ski_words = ['ski', 'skis', 'skiing', 'skier', 'snow', 'powder', 'slope']
tweets = ['Winter is coming! #thejoker @ Brian Head Ski Resort https://t.co/89LYVJWWgV',
          "NORDICA EXOPOWER TREND CX Ladies Women's SKI BOOTS w/ Ski/Walk Switch *SKIING Auction https://t.co/tTLiyHF6B8 OFFER https://t.co/xNAJKI1R1Y",
          "1CONSEIL si vous achetez des skis neufs FAITES REVISER VOS SEMELLES Ms skis @rossignol_1907 avaient toujours le fil. Chute et 1 an de galere",
          "I'm just sensitive to smell and my grandmother is applying the powder nonstop ever since she arrived to the house *massage my head*",
          "2omf baby daddy a powder head",
          "#atomic betty cartoon porn snow black porn https://t.co/R5pKHMSg2d",
          "mom still crying. i keep tearing up whenever Snow pops in my head. like thinking if he's in heaven right now running around with other cats.",
          "this not even me tweeting https://t.co/ZguXbjoUJu",
          "RT mariahgobrazy: guys don't understand that not giving a girl enough attention, lack of communication, and ignoring her can really fw"]

for tweet in tweets:
    tweet1 = tweet.lower()
    tweet1 = remove_characters(tweet1, "%:?&")
    print tweet_contains_words(tweet1, ski_words), tweet








