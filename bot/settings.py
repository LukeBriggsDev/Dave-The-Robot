from os import getenv

CLIENT_TOKEN = getenv("CLIENT_TOKEN")
CHANNEL_ID = int(getenv("CHANNEL_ID"))

FIELDS = ["comsci",
          "secres",
          "sofeng",
          "gameng"]

TOPICS = ["bio",
          "modelling",
          "hci",
          "games",
          "data"]

