# Get top fun facts from Reddit

import json
import urllib
from itertools import islice

import praw

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

reddit = praw.Reddit(client_id='Zm0DQg0eWYgPAg',
                     client_secret='7YL_cCBr1H2rFHaBcYEV977tlUU',
                     user_agent='Today I Learned by LysanderTheGreat v.1.0.0')

til = iter(reddit.subreddit('WritingPrompts').hot(limit=10))
try:
    nextTitle = str(nth(til, 3).title.encode('utf-8')).split("]")[1]
    print ('{} {}. Would you like another writing prompt?'.format("Writing Prompt:", nextTitle))
except Exception as e:
    print e
    print ('Sorry, there are no more prompts. Try again later!')

