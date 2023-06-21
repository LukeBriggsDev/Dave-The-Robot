import os
GENERAL_CHANNEL = os.environ.get("GENERAL_CHANNEL")
CLIENT_TOKEN = os.environ.get("CLIENT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
SERVER_2022_CHANNEL_ID = int(os.environ.get("SERVER_2022_CHANNEL_ID"))
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_CONSUMER_TOKEN = os.environ.get("TWITTER_CONSUMER_TOKEN")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
FIELDS = ["comsci", "secres", "sofeng", "gameng"]
SERVER_2020 = int(os.environ.get("SERVER_2020"))
ALLOWED_FUN_CHANNELS = [760486187349180447, 760488151331504229, 922169223789309965, 807000459155865600, 807070792902770708, 759501529752272978, 842049590194995241]
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
