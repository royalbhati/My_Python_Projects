#A simple reddit bot made by Royal Bhati (u/captainonboard) to warn users not use bad language 


import praw
import config

with open('foul_lang.txt') as f:
	foul_lang=f.read()


def bot_login():

	r=praw.Reddit(username=config.username,
				password=config.password,
				client_id=config.client_id,
				client_secret=config.client_secret,
				user_agent='Checking bad languages bot v1.0')
	return r

def run_bot(r):
	for comment in r.subreddit('testforlanguagebot').comments(limit=25):
		if comment.body in foul_lang:
			comment.reply('stop using bad language')
            # If you just want to have fun with the users and don't want to warn the use this reply 
            # comment.reply("""Why are you using this bad language?Don't use foul or abusive language. Let everything you say be good and helpful, (づ｡◕‿‿◕｡)づ  so that your words will be an encouragement to those who hear them.
             #cheers ヽ(◉◡◔)ﾉ """) 


r=bot_login()
run_bot(r)
