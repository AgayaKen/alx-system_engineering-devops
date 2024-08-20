#!/usr/bin/python3
"""
1-main
"""
import sys
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit=10"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("None")
        return
    
    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print("None")
            return
        
        for post in posts:
            print(post.get('data', {}).get('title'))
    except ValueError:
        print("None")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
