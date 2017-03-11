from datetime import datetime

def twitter_timestamp_to_python_date(d: str) -> datetime:
    """ Given a Twitter date-string,
    return a Python datetime.datetime object """
    return datetime.strptime(d, "%a %b %d %H:%M:%S +0000 %Y")

def python_to_twitter_until_date(d: datetime) -> str:
    """ Given a Python datetime.datetime instance,
    return a Twitter 'until:' date-string.
    (Which is NOT the same as a Twitter timestamp-string.) """
    return d.strftime("%Y-%m-%d")

def PrettyTweet(tweet):
    ts = twitter_timestamp_to_python_date(tweet['created_at']).strftime("%a %m/%d %H:%M")
    return "{}, {}, {}".format(ts, tweet["user"]["screen_name"], tweet["text"])
