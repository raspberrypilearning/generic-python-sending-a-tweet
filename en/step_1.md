You should already have authentication details for your app in **JSON** format before starting this section. If you have not yet registered an app with Twitter, then look at [this project]().

### Getting Tweepy

- The Python module you are going to use is called Tweepy. If it's not already on your computer, then you can install it using pip.

	```bash
	sudo pip3 install tweepy
	```

### Sending a tweet

- Open IDLE and create a new Python file. You could call it `tweeter.py`.

- Next you'll need to import the modules required for authentication and sending a tweet. The `tweepy` module lets you interact with the Twitter API. The `json` module is used to read your authentication data.

	```python
	import tweepy
	import json
	```

- Next you need to open the JSON file that contains your authentication data and read it all into your Python program. Make sure that your JSON file is in the same directory as the Python program you are writing.

	```python
	with open('twitterauth.json') as file:
		secrets = json.load(file)
	```

- You can run your program now if you like. If you type `secrets` into the shell, you'll see that your authentication details have been loaded into a [Python dictionary](link-to-python-dictionaries-ingredient).

- Now you need to provide your authentication details to the Twitter API. The following lines of code will load your details and prepare the API connection.

	```python
	auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
	auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

	twitter = tweepy.API(auth)
	```

- Lastly you can send a tweet with a single line of code.

	```python
	twitter.update_status('My first automated tweet!')
	```
	
- If you head on over to [Twitter.com](https://twitter.com) now, you should see that your tweet has been posted.

	![tweet](images/tweet1.png)

- Note that Twitter doesn't like duplicate tweets, so it you want to send another one, be sure to alter the string that you are sending.

### Sending an image

- If you want to send an image, then you can change the last line of code slightly.

	```python
	twitter.update_with_media('/path/to/image.jpg', 'your status update')
	```

	So if you had an image called `cat.png` in the same directory as your python file, it would be as simple as:
	
	```python
	twitter.update_with_media('cat.png', 'The Internet needs more cats.')
	```
	
	![cat tweet](images/tweet2.png)
