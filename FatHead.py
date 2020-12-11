import tweepy
import time
import random

auth = tweepy.OAuthHandler("w4J98Qk4qkD7yDAlVHb98p36b", "MnGJdovG5pdXUkETkxokGZTottP7G99p1mzLAYJULr7VI8JFkE")
auth.set_access_token("1302514377283731456-NqHIy9sBpxbdqIN9acZGzKbJpjTbT3", "HyVguC43mBsmpkaHuakb2yc9eI8KW1rNQ3PO40JewTyju")

api = tweepy.API(auth)

responses = ["BIG HEAD BIG HEAD", "Is it just me or is this guy's head like... weirdly big for his face?", "Oh god, do you think modern surgery could fix the uh, the face problem he's got?", "Oh no, dude's face is just too small :(", "I hope your face grows in soon! :)", "Hey Chuck, BIG FAN, why is your face so small? is it a medical condition?", "You know what they say about people with small faces lol", "This dude kinda looks like an alien tried to replicate a human but got the face proportions off, he looks fake", "#smallfacebighead", "bros head is just wayy too big for his face", "I hope your face gets bigger soon!", "SMALL FACE AHAHAHAH", "...big head...small face...hmmm"]
FILE_NAME = "RepliedTweets.txt"
def checkTweets(FILE_NAME):
    r = open(FILE_NAME, 'r')
    lastSeenID = int(r.read().strip())
    r.close()
    return lastSeenID

def storeTweet(FILE_NAME, ID):
    w = open(FILE_NAME, 'w')
    w.write(str(ID))
    w.close()
    return

tweets = api.user_timeline(checkTweets(FILE_NAME), screen_name = 'charliekirk11', count = 10, include_rts = False)

def reply():
    temp = checkTweets(FILE_NAME)
    tweets = api.user_timeline(since_id=temp, screen_name = 'charliekirk11', count = 10, include_rts = False)
    for tweet in reversed(tweets):
        response = responses[random.randint(0,13)]
        print(response)
        api.update_status("@" + tweet.user.screen_name + " " + response, tweet.id)
        storeTweet(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(10800)
