from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret will be generated for you after
consumer_key="aw0aDoq46cZb8JecQ8digA"
consumer_secret="OLLcjlLYzfW27DIfpsWIGLf2E8ZRgIdRanIU5Es0"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="48291909-MHzy05tIShIyBVunZsuPcjJo592hY1KhIyJFTlI"
access_token_secret="92uEdQXOR6mfaKrcMObkpSvXxl2AToqvkPW3PuiJc"

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)	
	#stream.filter(track=['Obama'],locations=[39.31,-76.59,38.89,-77.03,40.71,-74.00,38.71,-77.08])
	#stream.filter(locations=[-76.59,39.31,-77.03,38.89,-74.00,40.71,-77.08,38.71],track=["Obama"])
	sys.stdout = open("test.text","a")
	stream.filter(locations=[-77.03,38.8,-76.59,39.3])
	
	
	#out_file.write("%s" , stream.filter(locations=[-77.03,38.8,-76.59,39.3],track=["Obama"]))
	
