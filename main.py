from dataclasses import replace
from english_words import english_words_set
from numpy.random import poisson
import random
from time import sleep

import templates


########
# MAIN #
########

def main():
    while(True):
        tweet = generate_tweet()

        print(tweet)
        sleep(1)


######################
# GENERATE FUNCTIONS #
######################

def generate_tweet():
    tweet = random.choice(templates.tweets)
    tweet = tweet.replace("<BANDNAME>", generate_name())
    tweet = tweet.replace("<ALBUMNAME>", generate_album())
    return tweet

def generate_name():
    n_words = poisson(1)
    name = ""
    for word in range(n_words):
        name += random.choice(list(english_words_set)).capitalize() + " "
    return name + random.choice(list(english_words_set)).capitalize()

def generate_album():
    n_words = poisson(3)
    name = ""
    for word in range(n_words):
        name += random.choice(list(english_words_set)).capitalize() + " "
    return name + random.choice(list(english_words_set)).capitalize()

def generate_merch():
    pass

#######
# RUN #
#######

if __name__ == "__main__":
    main()
