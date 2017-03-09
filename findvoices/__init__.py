from findvoices.oauth import get_auth
from twitter import Twitter
import time

def PrettyTweet(tweet):
    ts = time.strftime('%a %m/%d %H:%M', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
    return "{}, {}, {}".format(ts, tweet["user"]["screen_name"], tweet["text"])

# Searches for tweets for each combination of search term and geolocation
def WordByLocationSearch(twit, search_list, geo_list):
    for s in search_list:
        for g in geo_list:
            print("Trying {} in {}".format(s, g[1]))
            d = twit.search.tweets(q=s, geocode=g[1])
            for status in d["statuses"]:
                print("{}, {}".format(g[0], PrettyTweet(status)))

def main():
    "Get some geolocated tweets."
    auth = get_auth()
    twit = Twitter(auth=auth)
    # Ohio searches
    WordByLocationSearch(twit, ["aca", "aca OR obamacare OR health insurance OR healthcare", "#SaveACA OR #ACAWorks OR #ProtectOurCare OR #MakeAmericaSickAgain"], [["Cleveland", "41.4993,-81.6944,100mi"], ["Columbus", "39.9612,-82.9988,50mi"]])


if __name__ == '__main__':
    main()
