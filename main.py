import tweepy
from dotenv import load_dotenv
import os
import requests
import random

# Loads the environment files form .env
load_dotenv()

bearer_token = os.environ["BEARER_TOKEN"]
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

client = tweepy.Client(
    bearer_token,
    api_key,
    api_secret,
    access_token,
    access_token_secret,
)


def main():
    print("Tweeting...\n")

    random_number = random.random()

    if random_number < 0.5:
        print("Tweeting a joke")
        tweet_joke(get_joke())
    else:
        print("Tweeting a quote")
        tweet_quote(get_quote())


def get_joke():
    jokes_api_url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart"
    respose = requests.get(url=jokes_api_url)

    joke = respose.json()

    return joke


def get_quote():
    quotes_api_url = "https://api.quotable.io/random?tags=technology"

    response = requests.get(url=quotes_api_url)

    quote = response.json()

    return quote


def tweet_joke(joke):
    tweet = f"{joke['setup']}\n\n\n{joke['delivery']}"

    client.create_tweet(text=tweet)


def tweet_quote(quote):
    tweet = f'"{quote["content"]}"\n\t\t\t-{quote["author"]}'

    client.create_tweet(text=tweet)


main()
