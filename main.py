import tweepy
from dotenv import load_dotenv
import os
import requests


def main():
    print("This is the main app")
    print(getJoke()["question"])
    print(getJoke()["punchline"])


def createTweet(
    text: str, poll_options: list[str] | None, poll_duration_in_days: int | None
):
    client = loadClient()

    # Convert poll duration to minutes
    poll_duaration = poll_duration_in_days * 24 * 31

    client.create_tweet(
        text=text, poll_options=poll_options, poll_duration_minutes=poll_duaration
    )


def loadClient():
    # Loads the environment files form .env
    load_dotenv()

    client = tweepy.Client(
        bearer_token=os.environ["BEARER_TOKEN"],
        consumer_key=os.environ["API_KEY"],
        consumer_secret=os.environ["API_KEY_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
    )

    return client


def getJoke():
    jokes_api_url = "https://backend-omega-seven.vercel.app/api/getjoke"
    respose = requests.get(url=jokes_api_url)

    joke = respose.json()

    return joke[0]


# Running the main app
main()
