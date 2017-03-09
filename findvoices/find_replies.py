from findvoices.oauth import get_auth
from twitter import Twitter
from datetime import datetime, timedelta

def twitter_timestamp_to_python_date(d: str) -> datetime:
    """ Given a Twitter date-string,
    return a Python datetime.datetime object """
    return datetime.strptime(d, "%a %b %d %H:%M:%S +0000 %Y")

def python_to_twitter_until_date(d: datetime) -> str:
    """ Given a Python datetime.datetime instance,
    return a Twitter 'until:' date-string.
    (Which is NOT the same as a Twitter timestamp-string.) """
    return d.strftime("%Y-%m-%d")

def find_replies(tweet_id: str, within_time: timedelta = timedelta(2)) -> dict:
    """ Get all(?) replies to the specified tweet """
    auth = get_auth()
    twit = Twitter(auth=auth)

    tweet = twit.statuses.show(_id=tweet_id)
    tweet_start = twitter_timestamp_to_python_date(tweet["created_at"])
    tweet_sn = tweet["user"]["screen_name"]

    # There doesn't appear to be a Twitter API for
    # "Get replies to this tweet."
    # But you can check whether a given tweet is a reply.
    # So, filter for replies to the user that were
    # sent after the tweet, and filter that resultset
    # locally to get actual replies.
    tweet_search_end = python_to_twitter_until_date(tweet_start + within_time)
    replies = twit.search.tweets(to=tweet_sn,
                                 since_id=tweet_id,
                                 until=tweet_search_end)
                                 
    return [x for x in replies["statuses"]
            if x["in_reply_to_status_id_str"] == tweet_id]

if __name__ == "__main__":
    print(find_replies("839183294876934144"))