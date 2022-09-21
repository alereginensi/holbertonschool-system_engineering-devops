#!/usr/bin/python3
'''
 function that queries the Reddit API and prints the titles 
 of the first 10 hot posts listed for a given subreddit.
'''
import requests

def top_ten(subreddit):
    '''queries the Reddit API'''
    try:
        url = 'http://reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }
        response = requests.get(url, headers=headers)
        for i in range (10):
            print(response.json()['data']['children'][i]['data']['title'])
    except Exception as e:
        print(None)
