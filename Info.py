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
    print(Fore.RED + "[{}]".format('-' * (lineLength-2)))
 
def printCredits():
    """ Prints out credits. Emphasis on perfected, look at how it looked on the 4th commit. You're welcome. """
    print(Style.BRIGHT + Fore.YELLOW + "Tool made by TheArchitect#8198".center(lineLength))
    print(Style.BRIGHT + Fore.YELLOW + "     perfected by jan Epiphany".center(lineLength))

def printTitle(title: str):
    """ Prints the logo with a section title embedded inside. """
    printSeparator()
    for line in logoASCII:
        print(Fore.CYAN + line.center(lineLength))
    print(Fore.GREEN + title.center(lineLength))
    printSeparator()
    printCredits()
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



def getName(randomProfile: RandomProfile):
    """ Name generator. """
    printTitle("NAME GENERATOR")

    choice = input("Full, First, or Last: ")
    sanatizedChoice = choice.lower()

    if sanatizedChoice == "full":
        print(f"Name: {randomProfile.full_name()[0]}")
    elif sanatizedChoice == "first":
        print(f"Name: {randomProfile.first_name()[0]}")
    elif sanatizedChoice == 'last':
        print(f"Name: {randomProfile.last_name()[0]}")
    else:
        print(f"Invalid option '{choice}'!")

def getAddress():
    """ Address generator. """
    printTitle("ADDRESS GENERATOR")

    state = input("Enter a two-letter state (e.x. CA CT VT AL AR DC FL GA KY TN MD OK TX): ")
    # real_random_address_by_state() only recognizes upper case charaters.
    address = real_random_address_by_state(state.upper())

    # real_random_address_by_state() can return an empty dict if no addresses could be found for the given state.
    if address: print(f"Address: {addressToString(address)}")
    else:       print(f"No addresses found for '{state}'")

def getNameAddress(randomProfile: RandomProfile):
    """ Name and address generator. """
    printTitle("Name+Address Gen")

    print(f"Name: {randomProfile.full_name()[0]}")
    print(f"Address: {addressToString(real_random_address())}")
    
def getGmail():
    """ Gmail generator. """
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    printTitle("GMAIL GENERATOR")
    print(random_char(7) + "@gmail.com")

def getProfile(randomProfile: RandomProfile):
    """ Profile generator. """
    printTitle("PROFILE GENERATOR")
    print("Profile : ")
    for property, value in randomProfile.full_profile()[0].items():
        print("\t{}: {}".format(property, value))



def main():
    # Initializes ANSI color code support for Windows if needed.
    colorama.init()
    randomProfile = RandomProfile()

    printTitle("Welcome to Random Information Generation")
    print(Fore.RED + "              Content Table")
    print(Fore.RED + " (1) Name Generator    (2) Address generator")
    print(Fore.RED + " (3) Name+Address       (4) Gmail generator")
    print(Fore.RED + "           (5) Profile Generator")
    printSeparator()

    option = input(Fore.GREEN + "Option: ")

    if option == '1':
        loopUntilStopped(getName, randomProfile)
    elif option == '2':
        loopUntilStopped(getAddress)
    elif option == '3':
        loopUntilStopped(getNameAddress, randomProfile)
    elif option == '4':
        loopUntilStopped(getGmail)
    elif option == '5':
        loopUntilStopped(getProfile, randomProfile)
    else:
        print(f"Invalid option '{option}'!")

if __name__ == '__main__':
    main()
