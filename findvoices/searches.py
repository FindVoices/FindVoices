from findvoices.oauth import get_auth
from twitter import Twitter
from datetime import datetime, timedelta

from utils import *

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

    return [PrettyTweet(x) for x in replies["statuses"]
            if x["in_reply_to_status_id_str"] == tweet_id]


# Geo list is made up of ["Location name", "lat:long:radius"] lists
def find_queries_by_locations(search_list: dict, geo_list: dict) -> list:
    """Does a search for each combination of search term and geo location"""
    auth = get_auth()
    twit = Twitter(auth=auth)

    l = []
    for s in search_list:
        for g in geo_list:
            d = twit.search.tweets(q=s, geocode=g[1])
            for status in d["statuses"]:
                l.append("{}, {}".format(g[0], PrettyTweet(status)))

    return l

if __name__ == "__main__":
    print("\n".join(find_replies("839183294876934144")))

    print("\n".join(find_queries_by_locations(
        ["aca OR obamacare OR health insurance OR healthcare",
         "#SaveACA OR #ACAWorks OR #ProtectOurCare OR #MakeAmericaSickAgain"],
        [["Cleveland", "41.4993,-81.6944,100mi"],
         ["Columbus", "39.9612,-82.9988,50mi"]])))
