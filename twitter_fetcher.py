import requests
from bearer_token import twitter_bearer_token
from config import OAuthEncodedToken


def get_trending_tags(woeid):
    response = send_request(twitter_bearer_token, woeid)
    if 'errors' in response and 'Invalid or expired token.' == response['errors'][0]['message']:
        token = get_new_token()
        response = send_request(token, woeid)
    if 'errors' in response and 'Sorry, that page does not exist.' == response['errors'][0]['message']:
        return []
    trends = response[0]['trends']

    result = []
    for tag in trends:
        result.append({'name': tag['name'], 'link': tag['url']})

    return result


def get_new_token():
    headers = {'Authorization': 'Basic ' + OAuthEncodedToken, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    response = requests.post('https://api.twitter.com/oauth2/token', data='grant_type=client_credentials', headers=headers).json()
    token = response['access_token']
    file = open('bearer_token.py', 'w')
    file.write("twitter_bearer_token = '" + token + "'")

    return token


def send_request(token, woeid):
    headers = {'Authorization': 'Bearer ' + token}

    return requests.get("https://api.twitter.com/1.1/trends/place.json?id=" + str(woeid), headers=headers).json()
