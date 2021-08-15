import tweepy

print('the bot is up and running... :D')

consumer_key = '' # The credentials are in develop
consumer_secret = '' # The credentials are in develop
key = '' # The credentials are in develop
secret = '' # The credentials are in develop

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
# api.update_status("I am alive")

FILE_NAME = 'last_seen.txt'

# def retrieve_last_seen_id(file_name):
#     f_read = open(file_name, 'r')
#     last_seen_id = int(f_read.read().strip())
#     f_read.close()
#     return last_seen_id

# def store_last_seen_id(id, file_name)
#     f_write = open(file_name, 'w')
#     f_write.write(str(last_seen_id))
#     f_write.close()
#     return

# tweets = api.mentions_timeline(retrieve_last_seen_id(FILE_NAME), tweet_mode='extended')
tweets = api.mentions_timeline()

for tweet in reversed(tweets):
    if '#caracolamagica' in tweet.text.lower():
      print(str(tweet.id) + ' - ' + tweet.text)
      api.update_status("@" + tweet.user.screen_name + " Qué onda ", tweet.id)
      # store_last_seen_id(FILE_NAEM, tweet.id)


