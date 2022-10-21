import random
import string
from typing import Any, Callable

from random_address import real_random_address_by_state, real_random_address
import colorama
from colorama import Fore, Style
from random_profile import RandomProfile

# All States Abbreviations are provided below
# CA
# CT
# VT
# AL
# AR
# DC
# FL
# GA
# KY
# TN
# MD
# OK
# TX


# Length each line printed.
lineLength = 44
logoASCII = [" ______    _   _               ",
             "|  ____|  | | | |              ",
             "| |__ __ _| |_| |__   ___ _ __ ",
             "|  __/ _` | __| '_ \ / _ \ '__|",
             "| | | (_| | |_| | | |  __/ |   ",
             "|_|  \__,_|\__|_| |_|\___|_|   "  ]

def printSeparator():
    """ Prints the separator bar used throughout the user interface. """
    print(end=Fore.RED)
    print("[{}]".format('-' * (lineLength-2)))

def printTitle(title: str):
    """ Prints the logo with a section title embedded inside. """
    printSeparator()

    print(end=Fore.CYAN)
    for line in logoASCII:
        print(line.center(lineLength))
    print(Fore.GREEN); print(title.center(lineLength))

    printSeparator()

    # Emphasis on perfected, look at how it was on the 4th commit. You're welcome.
    print(end=Fore.YELLOW)
    print("Tool made by TheArchitect#8198".center(lineLength))
    print("     perfected by jan Epiphany".center(lineLength))

    printSeparator()

def askToContinue() -> bool:
    """ Asks the user if they would like to continue, returning True for yes and False for no. """
    while True:
        choice = input("Would you like to continue? [Y/N]: ")
        if not choice:
            continue

        sanatizedChoice = choice[0].lower()

        if sanatizedChoice == 'y':
            return True
        elif sanatizedChoice == 'n':
            return False
        else:
            print(f"Invalid option '{choice}'!")

def loopUntilStopped(function: Callable[..., None], *arguments: Any):
    """ Continuosly runs the given the function, asking the user if they would like to continue every iteration. Will run until
        they say no. """
    while True:
        function(*arguments)

        if not askToContinue():
            break



def addressToString(address: dict) -> str:
    """ Converts the addresses produced by Random Address into a human-readable string. """
    return f"{address['address1']}, {address['city']}, {address['state']} {address['postalCode']}, USA"



def getName(randomGenerator: RandomProfile):
    """ Name generator. """
    printTitle("NAME GENERATOR")
    print(end=Fore.GREEN)

    choice = input("Full, First, or Last: ")
    sanatizedChoice = choice.lower()

    if sanatizedChoice == "full":
        print(f"Name: {randomGenerator.full_name()[0]}")
    elif sanatizedChoice == "first":
        print(f"Name: {randomGenerator.first_name()[0]}")
    elif sanatizedChoice == 'last':
        print(f"Name: {randomGenerator.last_name()[0]}")
    else:
        print(f"Invalid option '{choice}'!")

def getAddress():
    """ Address generator. """
    printTitle("ADDRESS GENERATOR")
    print(end=Fore.GREEN)

    state = input("Enter a two-letter state (e.x. CA CT VT AL AR DC FL GA KY TN MD OK TX): ")
    # real_random_address_by_state() only recognizes upper case charaters.
    address = real_random_address_by_state(state.upper())

    # real_random_address_by_state() can return an empty dict if no addresses could be found for the given state.
    if address: print(f"Address: {addressToString(address)}")
    else:       print(f"No addresses found for '{state}'")

def getNameAddress(randomGenerator: RandomProfile):
    """ Name and address generator. """
    printTitle("Name+Address Gen")
    print(end=Fore.GREEN)

    print(f"Name: {randomGenerator.full_name()[0]}")
    print(f"Address: {addressToString(real_random_address())}")
    
def getGmail():
    """ Gmail generator. """
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    printTitle("GMAIL GENERATOR")
    print(end=Fore.GREEN)

    print(random_char(7) + "@gmail.com")

def getProfile(randomGenerator: RandomProfile):
    """ Profile generator. """
    printTitle("PROFILE GENERATOR")
    print(end=Fore.GREEN)

    print("Profile : ")
    for property, value in randomGenerator.full_profile()[0].items():
        print("\t{}: {}".format(property, value))



def main():
    randomGenerator = RandomProfile()
    # Initializes ANSI color code support for Windows if needed.
    colorama.init()
    # Makes all colors bright for that extra A E S T H E T I C.
    print(end=Style.BRIGHT)

    while True:
        printTitle("Welcome to Random Information Generation")

        print(end=Fore.GREEN)
        print("Content Table".center(lineLength))
        print("(1) Name Generator     (2) Address generator".center(lineLength))
        print("(3) Name+Address       (4) Gmail generator  ".center(lineLength))
        print("(5) Profile Generator  (6) Exit             ".center(lineLength))
        printSeparator()

        print(end=Fore.GREEN); option = input("Option: ")

        if option == '1':
            loopUntilStopped(getName, randomGenerator)
        elif option == '2':
            loopUntilStopped(getAddress)
        elif option == '3':
            loopUntilStopped(getNameAddress, randomGenerator)
        elif option == '4':
            loopUntilStopped(getGmail)
        elif option == '5':
            loopUntilStopped(getProfile, randomGenerator)
        elif option == '6':
            break
        else:
            print(end=Fore.RED); print(f"Invalid option '{option}'!")

if __name__ == '__main__':
    main()
