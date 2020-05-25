import praw

reddit = praw.Reddit(client_id='', client_secret='', username = '', password = '', user_agent = '')

subreddit = reddit.subreddit('')

keysList = []

def setRedditInfo()
	new_clientID = input("Enter the Client ID: ")
	new_clientSecret = input("Enter the Client Secret: ")
	new_username = input("Enter the Username of the bot: ")
	new_password = input("Enter the Password of the bot: ")
	new_agent = input("Enter the User Agent: ")

	reddit = praw.Reddit(client_id = new_clientID, client_secret = new_clientSecret, username = new_username, password = new_password, user_agent = new_agent)
 
def promptActions()
	print("What would you like to do:")
	print("   a) Set info for the Reddit bot.")
	print("   b) Add a Subreddit to monitor.")
	print("   c) Remove a monitored Subreddit.")
	print("   d) Add a keyphrase to look for.")
	print("   e) Remove a keyphrase being looked for.")
	print("   f) Set a responce when keyphrase is found.") # TODO: different responces for different keywords (likely done with dictionaries)
	print("   g) Exit program.")
	responce = input("Enter the corresponding letter: ")
	if lower(responce) == "g" : 
		quit()
	elif lower(responce) == "a" :
			setRedditInfo()
	elif lower(responce) == "b" :
			addSubreddit()
	elif lower(responce) == "c" :
			removeSubreddit()
	elif lower(responce) == "d" :
			addWord()
	elif lower(responce) == "e" :
			removeWord()
	elif lower(responce) == "f" :
			setResponce()
	else:
			promptActions() 

def addSubreddit()

def removeSubreddit()

def removeWord()

def addWord()
	cont = "yes"
	while( cont == "yes")
		wordToAdd = input("Enter a keyphrase to watch for: ")
		print("Keyphrase list is now: ")
		for x in keysList:
			print(keysList[x])
		cont = lower(input("Do you have more keyphrases to enter? (Yes / No)"))

def isWord(word)
	return word in keysList

def setResponce()