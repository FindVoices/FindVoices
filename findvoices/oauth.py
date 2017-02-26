"""
Do what is necessary to authenticate this tester as a Twitter "app", using
somebody's Twitter account.
"""
import os
from getpass import getpass
from twitter.oauth import OAuth
from twitter import oauth_dance, read_token_file, TwitterHTTPError


AUTH_TOKEN_PATH = os.path.expanduser('~/.cache/oauth/twitter_findvoices.auth')
APP_TOKEN_PATH = os.path.expanduser('~/.cache/oauth/twitter_findvoices_app.auth')


def get_consumer_secret():
    if os.path.exists(APP_TOKEN_PATH):
        return open(APP_TOKEN_PATH).read()

    token = getpass(prompt='Enter the application secret for FindVoices (get it from Rob): ')
    os.makedirs(os.path.dirname(APP_TOKEN_PATH), exist_ok=True)
    with open(APP_TOKEN_PATH, 'w') as out:
        out.write(token)
    return token


def get_auth():
    consumer_key = '2KgMeaDVntA0ecc6Giri8ly4e'

    if os.path.exists(AUTH_TOKEN_PATH):
        token, token_secret = read_token_file(AUTH_TOKEN_PATH)
    else:
        authdir = os.path.dirname(AUTH_TOKEN_PATH)
        if not os.path.exists(authdir):
            os.makedirs(authdir)
        try:
            token, token_secret = oauth_dance(
                app_name='findvoices',
                consumer_key=consumer_key,
                consumer_secret=get_consumer_secret(),
                token_filename=AUTH_TOKEN_PATH
            )
        except TwitterHTTPError:
            # Auth failed. We might have the wrong token.
            os.unlink(APP_TOKEN_PATH)

    return OAuth(
        token=token,
        token_secret=token_secret,
        consumer_key=consumer_key,
        consumer_secret=get_consumer_secret()
    )


if __name__ == '__main__':
    get_auth()
    print("Yay, you're authenticated!")
