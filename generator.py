import random
from english_words import get_english_words_set
from numpy.random import poisson
import bot_templates

_word_set = None

def get_word_list():
    global _word_set
    if _word_set is None:
        _word_set = list(get_english_words_set(["web2"]))
    return _word_set

def generate_name(word_set=None):
    if word_set is None:
        word_set = get_word_list()
    n_words = poisson(1)
    name = ""
    for _ in range(n_words):
        name += random.choice(word_set).capitalize() + " "
    return (name + random.choice(word_set).capitalize()).strip()

def generate_album(word_set=None):
    if word_set is None:
        word_set = get_word_list()
    n_words = poisson(2)
    name = ""
    for _ in range(n_words):
        name += random.choice(word_set).capitalize() + " "
    return (name + random.choice(word_set).capitalize()).strip()

def generate_tweet(word_set=None, band_name=None, album_name=None):
    if word_set is None:
        word_set = get_word_list()
    if band_name is None:
        band_name = generate_name(word_set)
    if album_name is None:
        album_name = generate_album(word_set)

    tweet = random.choice(bot_templates.tweets).strip()
    tweet = tweet.replace("<BANDNAME>", band_name)
    tweet = tweet.replace("<ALBUMNAME>", album_name)
    return {
        "band_name": band_name,
        "album_name": album_name,
        "tweet": tweet
    }
