from discord.ext.commands import Cog, command, check
from bot.settings import CHANNEL_ID, FIELDS, TWITTER_ACCESS_TOKEN, TWITTER_BEARER_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_CONSUMER_TOKEN, TWITTER_CONSUMER_SECRET
from threading import Thread
import schedule
import tweepy
import os
from time import sleep

class Tweet(Cog):
  def __init__(self, bot):
      self.bot = bot
      auth = tweepy.OAuthHandler(TWITTER_CONSUMER_TOKEN,
                                 TWITTER_CONSUMER_SECRET)
      auth.set_access_token(TWITTER_ACCESS_TOKEN,
                            TWITTER_ACCESS_TOKEN_SECRET)
      self.api = tweepy.API(auth)
      self.api.verify_credentials()
      print("verified")
      schedule.every().monday.at("20:00").do(self.tweet)
      schedule.every().wednesday.at("20:00").do(self.tweet)
      schedule.every().friday.at("20:00").do(self.tweet)
      thread = Thread(target=self.start_tweeting)
      thread.start()
  
  def start_tweeting(self):
      while (True):
          schedule.run_pending()
          sleep(1)

  def tweet(self):
      text = self.get_wisdom_list()
      with open(os.path.dirname(__file__) + "/tweet.txt", "r+") as f:
          index = int(f.read())
          choice = text[index]
          status = self.api.update_status(status=choice)
          print("tweeted")
          f.seek(0)
          f.write(str(index + 1))
          f.flush()
          os.fsync(f.fileno())

      print(choice)

  def get_wisdom_list(self):
      with open(
              os.path.dirname(__file__) + "/../media/jokesandquotes.txt",
              "r") as f:
          text = f.read().split("%")
          return text


def setup(bot):
  bot.add_cog(Tweet(bot))