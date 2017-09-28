from flask import Flask, redirect, request
from aweber_api import AWeberAPI

app = Flask(__name__)
url = 'http://localhost:5000'
consumer_key = 'AkahU7LuENNRNz4YEU1t0gYf'
consumer_secret = 'zgyp6JxNMDWH0uqgdet8MQy4qb3UZh7S6dDsEnwX'
aweber = AWeberAPI(consumer_key, consumer_secret)


@app.route('/')
def hello():
    request_token, request_token_secret = aweber.get_request_token(url + '/callback')
    print "request token " + request_token
    print "secret " + request_token_secret
    aweber.user.token_secret = request_token_secret

    authorization_url = aweber.authorize_url

    return redirect(authorization_url)

@app.route('/callback')
def callback():
    request_token = request.args.get('oauth_token')
    verifier = request.args.get('oauth_verifier')
    aweber.user.verifier = verifier
    aweber.user.request_token = request_token

    print "verifier " + verifier
    print "token " + request_token

    access_token, access_token_secret = aweber.get_access_token()

    return access_token

if __name__ == '__main__':
    app.run()
