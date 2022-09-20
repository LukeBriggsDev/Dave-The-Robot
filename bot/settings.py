from os import getenv

GENERAL_CHANNEL = getenv("GENERAL_CHANNEL")
CLIENT_TOKEN = getenv("CLIENT_TOKEN")
CHANNEL_ID = int(getenv("CHANNEL_ID"))
SERVER_2022_CHANNEL_ID = int(getenv("SERVER_2022_CHANNEL_ID"))
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_CONSUMER_TOKEN = getenv("TWITTER_CONSUMER_TOKEN")
TWITTER_CONSUMER_SECRET = getenv("TWITTER_CONSUMER_SECRET")
FIELDS = ["comsci", "secres", "sofeng", "gameng"]
SERVER_2020 = int(getenv("SERVER_2020"))
PRONOUNS = [
    "he/him",
    "she/her",
    "they/them",
    "he/they",
    "she/they",
    "any pronouns",
    "neopronouns",
    "name only",
    "ask pronouns",
]

TOPICS = ["bio", "modelling", "hci", "games", "data"]

STAGE_3_MODULES = [
    "csc3121 (Distributed Systems)",
    "csc3131 (Development and Operations of Systems)",
    "csc3132 (Introduction to Quantum Computing)",
    "csc3231 (Graphics for Games)",
    "csc3232 (Gaming Technologies and Simulations)",
    "csc3332 (Abstract models of Systems & Languages)",
    "csc3333 (Understanding Concurrency)",
    "csc3431 (Introduction to BioDesign and Natural Computing)",
    "csc3432 (Biomedical Data Analytics and A)I", "csc3631 (Cryptography)",
    "csc3632 (System and Network Security)",
    "csc3634 (Fault Tolerant and Cyber-Physical Systems)",
    "csc3731 (Human Computer Interaction: Interaction Design)",
    "csc3831 (Predictive Analytics, Computer Vision & AI)",
    "csc3833 (Data Visualization and Visual Analytics)"
]
