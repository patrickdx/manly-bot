from random import randint

import praw
import random
import config


def main():
    reddit = praw.Reddit(client_id="config.ID",
    client_secret="config.secret",
    user_agent="config.user_agent",
    username="manly-bot",
    password="config.password")

    for comment in reddit.subreddit("forsen").stream.comments(skip_existing=True):      #indefinitely iterate over NEW comments, skip_existing=True as parameter to start recieving new comments after stream is created. # +"test" for more subreddits
        print(comment.body)
        if comment.body == "!manly":
            author = reddit.redditor(comment.author)
            # comment.reply(manly(author))
            print(manly(author))

        else:                                               #!manly word
            try:                                                        #try so no index out of bounds
                print(comment.body.split(" ")[1])                                                          #take 2nd word

                if comment.body == "!manly " + comment.body.split(" ")[1] and charcheck(comment.body.split(" ")[1]):                        #check if 2nd word is char and in the form !manly word
                    print("no chars")
                    author = reddit.redditor(comment.body.split(" ")[1])
                    # comment.reply(manly(author))
                    print(manly(author))

            except IndexError:          #pass if index out of bounds
                pass


def charcheck(comment):     # if special characters are in comment
    char = "!@#$%^&*()"
    for i in char:
        if i in comment:             # if special char is detected
            return False
    return True

def manly(author):

    if "billy" in str(author.name):
        rand = randint(90, 100)
    else:
        rand = randint(0, 100)

    if 0 <= rand <= 20:
        emote = "nymnSoyBoy"

    elif 20 < rand <= 40:
        emote = "doctorBANGS"

    elif 40 < rand <= 60:
        emote = "doctorPUNK"

    elif 60 < rand < 70:
        emote = "gachiBASS"

    elif 70 <= rand <= 80:
        emote = "forsenReady"

    elif 80 < rand <= 90:
        emote = "billyReady"

    elif 100 != rand >= 90:
        emote = "gachiHYPER"

    elif rand == 100:
        emote = "gachiApprove"

    return str(author.name) + " is " + str(rand) + "%" + " manly! " + emote


if __name__ == "__main__":  # call main only in the cases that this script is the one being executed:
    main()
