from os import getenv

CLIENT_TOKEN = getenv("CLIENT_TOKEN")
CHANNEL_ID = int(getenv("CHANNEL_ID"))
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_CONSUMER_TOKEN = getenv("TWITTER_CONSUMER_TOKEN")
TWITTER_CONSUMER_SECRET = getenv("TWITTER_CONSUMER_SECRET")
FIELDS = ["comsci",
          "secres",
          "sofeng",
          "gameng"]

TOPICS = ["bio",
          "modelling",
          "hci",
          "games",
          "data"]

