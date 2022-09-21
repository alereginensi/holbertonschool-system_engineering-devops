#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers for a given subreddit.'''
'''If an invalid subreddit is given, the function should return 0.'''

import requests
import sys

def number_of_subscribers(subreddit):
    '''queries the Reddit API'''
    try:
        reddit = sys.argv[1]
        url = 'http://reddit.com/r/{}/about.json'.format(reddit)
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }

        response = requests.get(url, headers=headers).json()
        subs = response['data']['subscribers']
        return subs
    except(Exception) as error:
        return 0
