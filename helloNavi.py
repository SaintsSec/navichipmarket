# A simple helloworld for the chip market

import getpass

command = "/hellonavi"
use = "Chip Market Works"
user = getpass.getuser()


def run():
    print(f"Navi> Hello {user}! Welcome to the Chip Market!")
