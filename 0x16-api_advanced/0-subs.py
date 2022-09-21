#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.
'''
import requests


def number_of_subscribers(subreddit):
    '''queries the Reddit API'''
    try:
        url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }
        response = requests.get(url, headers=headers)
        return response.json()['data']['subscribers']
    except Exception as e:
        return 0
