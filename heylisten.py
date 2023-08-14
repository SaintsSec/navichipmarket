import time
import random

command = "/heylisten"
use = "Annoying... "


def typewriter(text):
    for char in text:
        print(char, end="", flush=True,)
        # generate a random number between 0 and 1
        random_num = random.uniform(0, 1)
        # if the random number is less than .1
        if random_num < .1:
            # sleep for 1 second
            time.sleep(.0)
        # else if the rando
        elif random_num < .2:
            # sleep for .5 seconds
            time.sleep(.050)
        # else
        else:
            # sleep for .1 seconds
            time.sleep(.010)


def run():
    typewriter(
        "\nNavi> Hey!! Listen!!! WATCH OUT!!\nNavi> Sorry, hold on... this is not the right Easter egg ...\n")
    print("")
    typewriter("Navi> *Anime style air jump* Navi!!! Jack-In EXECUTE!!!")
    print("")
    typewriter("Navi> *sigh* There now I don't feel so dirty...*eye-roll*")
    print("")
