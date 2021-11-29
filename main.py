import requests
import tweepy

#get followers from twitter api
auth = tweepy.OAuthHandler('', '')
api = tweepy.API(auth)
user = '@' + input('Enter the twitter handle: ')
def get_followers(user):
    followers = []
    for page in tweepy.Cursor(api.followers, screen_name=user).pages():
        followers.extend(page)
    print(followers)        
get_followers(user)
#get friends from twitter api
# def get_friends(user):
#     friends = []
#     for page in tweepy.Cursor(api.friends, screen_name=user).pages():
#         friends.extend(page)
#     return friends


