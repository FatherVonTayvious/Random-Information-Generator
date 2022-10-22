#!/usr/bin/env python3

"""
A command-line tool for randomly generating various kinds of information.

authors: TheArchitect#8198,
         ona li toki e jan Epiphany tawa mi
 ______    _   _
|  ____|  | | | |
| |__ __ _| |_| |__   ___ _ __
|  __/ _` | __| '_ \ / _ \ '__|
| | | (_| | |_| | | |  __/ |
|_|  \__,_|\__|_| |_|\___|_|
"""

import random
import secrets
import string
from typing import Any, Callable, Sequence, Tuple

import colorama
from colorama import Fore, Style
from random_address import real_random_address, real_random_address_by_state
from random_profile import RandomProfile
from random_profile.main import email_domains

# Length of each line printed.
lineLength = 50
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

def inputNumberSafely(prompt: object=..., canNegative: bool=True) -> int:
    """ Prints the prompt to the user and returns the number they give. Should they not give a valid number it will ask them until
        they do. If canNegative is False it will not accept negative numbers, make sure to tell user if necessary. """
    while True:
        choice = input(prompt)

        try:
            choice = int(choice)
            if not canNegative and choice < 0: raise ValueError
                
            return choice

        except ValueError:
            print(f"Invalid number '{choice}'!")

def askToContinue() -> bool:
    """ Asks the user if they would like to continue, returning True for yes and False for no. """
    while True:
        choice = input("Would you like to continue? [Y/n]: ")
        if not choice:
            continue

        sanatizedChoice = choice[0].strip().lower()

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

def addressToCoordinates(address: dict) -> Tuple[int, int]:
    """ Extracts coordinates from the addresses produced by Random Address"""
    coordinates = address['coordinates']
    return (coordinates['lat'], coordinates['lng'])

def _randomString(choiceFunction: Callable[[Sequence], Any], length: int) -> str:
    """ Common code for random string generation to avoid code duplication. """
    return ''.join(choiceFunction(_randomString.alphanumerics) for _ in range(length))

_randomString.alphanumerics = string.ascii_letters + string.digits

def randomString(length: int) -> str:
    """ Generates a string of randomly-selected alphanumeric characters of the given length. """
    return _randomString(random.choice, length)

def randomStringSecure(length: int) -> str:
    """ Generates a string of randomly-selected alphanumeric characters of the given length using the secrets module."""
    return _randomString(secrets.choice, length)



def nameMenu(randomGenerator: RandomProfile):
    """ Name generator. """
    print(end=Fore.GREEN)

    choice = input("Full, first, or last name?: ")
    sanatizedChoice = choice.strip().lower()
    chosenGenerator = None

    if sanatizedChoice == "full":
        chosenGenerator = randomGenerator.full_name
    elif sanatizedChoice == "first":
        chosenGenerator = randomGenerator.first_name
    elif sanatizedChoice == 'last':
        chosenGenerator = randomGenerator.last_name
    else:
        print(f"Invalid option '{choice}'!")
        return

    times = inputNumberSafely("How many to generate?: ", canNegative=False)
    for i in range(1, times + 1):
        print(f"Name {i}: {chosenGenerator()[0]}")

def addressMenu():
    """ Address generator. """
    print(end=Fore.GREEN)

    state = input("Enter a two-letter state (e.x. CA CT VT) to pull addresses from. Enter nothing for all states: ")
    # real_random_address_by_state() only recognizes upper case charaters.
    sanatizedState = state.strip().upper()
    times = inputNumberSafely("How many would you like to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        address = real_random_address_by_state(sanatizedState) if state else real_random_address()

        if address: 
            print(f"Address {i}: {addressToString(address)}")
        else:       
            print(f"{i}: No addresses found for '{state}'")

def passwordMenu():
    """ Password generator. """
    print(end=Fore.GREEN)

    length = inputNumberSafely("Enter the length of the password: ", canNegative=False)
    times = inputNumberSafely("How many to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        print(f"Password {i}: {randomStringSecure(length)}") 
    
def emailMenu(randomGenerator: RandomProfile):
    """ Email generator. """
    print(end=Fore.GREEN)

    times = inputNumberSafely("How many to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        print("Email {}: {}.{}{}@{}".format(
                i,
                randomGenerator.last_name()[0].lower(),
                randomGenerator.first_name()[0].lower(),
                randomString(random.randint(3, 7)),
                random.choice(email_domains)))

def profileMenu(randomGenerator: RandomProfile):
    """ Profile generator. """
    print(end=Fore.GREEN)

    times = inputNumberSafely("How many to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        print(f"Profile {i}:")
        for property, value in randomGenerator.full_profile()[0].items():
            print("\t{}: {}".format(property, value))

def coordinateMenu():
    """ Coordinate generator. """
    print(end=Fore.GREEN)

    state = input("Enter a two-letter state (e.x. CA CT VT) to pull coordinates from. Enter nothing for all states: ")
    # real_random_address_by_state() only recognizes upper case charaters.
    sanatizedState = state.strip().upper()
    times = inputNumberSafely("How many to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        address = real_random_address_by_state(sanatizedState) if sanatizedState else real_random_address()

        if address:
            coordinates = addressToCoordinates(address)
            print("Coordinate {}: ({:.6f}, {:.6f})".format(i, coordinates[0], coordinates[1]))
        else:       
            print(f"{i}: No coordinates found for '{state}'")



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
        print("(1) Name generator     (2) Address generator   ".center(lineLength))
        print("(3) Password generator (4) Email generator     ".center(lineLength))
        print("(5) Profile generator  (6) Coordinate generator".center(lineLength))
        print("(7) Exit                                       ".center(lineLength))
        printSeparator()

        option = None

        # Inner loop so that title and select menu don't continuosly clutter the interface.
        while True:
            print(end=Fore.GREEN); option = input("Option: ")
            sanatizedOption = option.strip()

            if sanatizedOption == '1':
                printTitle("NAME GENERATOR")
                loopUntilStopped(nameMenu, randomGenerator)
            elif sanatizedOption == '2':
                printTitle("(REAL) ADDRESS GENERATOR")
                loopUntilStopped(addressMenu)
            elif sanatizedOption == '3':
                printTitle("PASSWORD GENERATOR")
                loopUntilStopped(passwordMenu)
            elif sanatizedOption == '4':
                printTitle("EMAIL GENERATOR")
                loopUntilStopped(emailMenu, randomGenerator)
            elif sanatizedOption == '5':
                printTitle("(FAKE) PROFILE GENERATOR")
                loopUntilStopped(profileMenu, randomGenerator)
            elif sanatizedOption == '6':
                printTitle("(USA) COORDINATE GENERATOR")
                loopUntilStopped(coordinateMenu)
            elif option != '7':
                # No need to print an error if they typed nothing.
                if sanatizedOption:
                    print(end=Fore.RED); print(f"Invalid option '{option}'!")
                continue

            break

        if option == '7':
            break

if __name__ == '__main__':
    main()
