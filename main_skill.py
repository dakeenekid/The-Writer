from flask import Flask
from flask_ask import Ask, question, statement
from itertools import islice
import praw
import keys

count = 2

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

app = Flask(__name__)
ask = Ask(app,"/")

@ask.launch
def greet():
    response = "Welcome to The Writer, a Reddit Writing Prompt Alexa Skill. Would you like a prompt?."
    return question(response)

@ask.intent('YesIntent')
def getTIL():
    global count
    reddit = praw.Reddit(client_id=keys.client_id,
                         client_secret=keys.client_secret,
                         user_agent=keys.user_agent)

    til = iter(reddit.subreddit('WritingPrompts').hot(limit=50))
    try:
        nextTitle = str(nth(til, count).title.encode('utf-8')).split("]")[1]
        count = count + 1
        return question('{},{}. Would you like another writing prompt?'.format("Writing Prompt:",nextTitle))
    except Exception as e:
        print e
        return statement('Sorry, there are no more prompts. Try again later!')

@ask.intent('NoIntent')
def sayNo():
    global count
    response = "Okay, I'm always available to help if you need a writing prompt!"
    count = 2
    return statement(response)

@ask.intent('HelpIntent')
def sayHelp():
    return question('This skill provides random writing prompts from the Writing Prompts subreddit. Would you like a prompt?')

if __name__ == '__main__':
    app.run(debug=True)