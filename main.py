from dataclasses import replace
from english_words import get_english_words_set
from numpy.random import poisson
import random
from time import sleep

import templates


########
# MAIN #
########

def main():
    ws = list(get_english_words_set(["web2"]))
    while(True):
        tweet = generate_tweet(ws)

        print(tweet)
        sleep(1)


######################
# GENERATE FUNCTIONS #
######################

def generate_tweet(word_set):
    tweet = random.choice(templates.tweets)
    tweet = tweet.replace("<BANDNAME>", generate_name(word_set))
    tweet = tweet.replace("<ALBUMNAME>", generate_album(word_set))
    return tweet

def generate_name(word_set):
    n_words = poisson(1)
    name = ""
    for word in range(n_words):
        name += random.choice(word_set).capitalize() + " "
    return name + random.choice(word_set).capitalize()

def generate_album(word_set):
    n_words = poisson(3)
    name = ""
    for word in range(n_words):
        name += random.choice(word_set).capitalize() + " "
    return name + random.choice(word_set).capitalize()

def generate_merch():
    pass

#######
# RUN #
#######

if __name__ == "__main__":
    main()
