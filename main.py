from time import sleep
import generator

########
# MAIN #
########

def main():
    word_set = generator.get_word_list()
    while True:
        data = generator.generate_tweet(word_set)
        print(data["tweet"])
        sleep(1)

#######
# RUN #
#######

if __name__ == "__main__":
    main()
