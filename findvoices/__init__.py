from findvoices.oauth import get_auth
from twitter import Twitter


def main():
    "Get some geolocated tweets."
    auth = get_auth()
    twit = Twitter(auth=auth)
    # I don't even know where this is
    print(twit.search.tweets(geocode="37.781157,-122.398720,1mi"))


if __name__ == '__main__':
    main()