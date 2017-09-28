from aweber_api import AWeberAPI
from flask import Flask


def getKey():
    url = 'http://localhost:5000'
    consumer_key = 'AkahU7LuENNRNz4YEU1t0gYf'
    consumer_secret = 'zgyp6JxNMDWH0uqgdet8MQy4qb3UZh7S6dDsEnwX'
    aweber = AWeberAPI(consumer_key, consumer_secret)

    request_token, request_token_secret = aweber.get_request_token(url + '/callback')
    print request_token
    print request_token_secret

    print aweber.authorize_url

    redirect(authorization_url)

    aweber.user.verifier = verifier
    aweber.user.request_token = request_token
    aweber.user.token_secret = request_token_secret
    access_token, access_token_secret = aweber.get_access_token()

    print access_token

if __name__ == '__main__':
    getKey()
