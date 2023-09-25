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

---

This file is part of Random-Information-Generator.

Random-Information-Generator is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

Random-Information-Generator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
Random-Information-Generator. If not, see <https://www.gnu.org/licenses/>.
"""

import random
import secrets
import string
from typing import Any, Callable, Sequence, Tuple

import colorama
from colorama import Fore, Style
from random_address import real_random_address, real_random_address_by_state
from random_profile import RandomProfile



# Email domains for the email generator.
email_domains = [ "gmail.com", "yahoo.com", "hotmail.com", "aol.com"
                , "hotmail.co.uk", "hotmail.fr", "msn.com", "yahoo.fr"
                , "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk"
                , "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com"
                , "free.fr", "gmx.de", "web.de", "yandex.ru", "ymail.com"
                , "libero.it", "outlook.com", "uol.com.br", "bol.com.br"
                , "mail.ru", "cox.net", "hotmail.it", "sbcglobal.net", "sfr.fr"
                , "live.fr", "verizon.net", "live.co.uk", "bigpond.com"
                , "terra.com.br", "yahoo.it", "neuf.fr", "alice.it"
                , "rocketmail.com", "att.net", "laposte.net", "facebook.com"
                , "bellsouth.net", "yahoo.in", "hotmail.es" ]



# Length of each line printed.
lineLength = 50
logoASCII = [ r" ______    _   _               "
            , r"|  ____|  | | | |              "
            , r"| |__ __ _| |_| |__   ___ _ __ "
            , r"|  __/ _` | __| '_ \ / _ \ '__|"
            , r"| | | (_| | |_| | | |  __/ |   "
            , r"|_|  \__,_|\__|_| |_|\___|_|   "
            ]

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

    print(end=Fore.YELLOW)
    print("Tool made by TheArchitect#8198".center(lineLength))
    print("     perfected by jan Epiphany".center(lineLength))

    printSeparator()

def inputNumberSafely(prompt: object=..., canNegative: bool=True) -> int:
    """ Prints the prompt to the user and returns the number they give. Should they not give a valid number it will ask them until
        they do. If canNegative is False it will not accept negative numbers, make sure to tell user if necessary. """
    while True:
        print(end=Fore.GREEN)
        choice = input(prompt)

        try:
            choice = int(choice)
            if not canNegative and choice < 0: raise ValueError

            return choice

        except ValueError:
            print(end=Fore.RED)
            print(f"Invalid number '{choice}'!")

def askToContinue() -> bool:
    """ Asks the user if they would like to continue, returning True for yes and False for no. """
    while True:
        print(end=Fore.GREEN)
        choice = input("Would you like to continue? [Y/n]: ")
        if not choice:
            continue

        sanatizedChoice = choice.strip()[0].lower()

        if sanatizedChoice == 'y':
            return True
        elif sanatizedChoice == 'n':
            return False
        else:
            print(end=Fore.RED)
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
        chosenGenerator = randomGenerator.full_names
    elif sanatizedChoice == "first":
        chosenGenerator = randomGenerator.first_names
    elif sanatizedChoice == 'last':
        chosenGenerator = randomGenerator.last_names
    else:
        print(f"Invalid option '{choice}'!")
        return

    times = inputNumberSafely("How many to generate?: ", canNegative=False)
    for i in range(1, times + 1):
        print(f"Name {i}: {chosenGenerator()}")

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

    domain = input("Enter a domain to use (e.x. gmail.com.) Leave blank to have one randomly"
                   " selcted: ").strip()
    times = inputNumberSafely("How many to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        print("Email {}: {}.{}{}@{}".format(
                i,
                randomGenerator.last_names().lower(),
                randomGenerator.first_names().lower(),
                randomString(random.randint(3, 7)),
                domain if domain else random.choice(email_domains)))

def profileMenu(randomGenerator: RandomProfile):
    """ Profile generator. """
    print(end=Fore.GREEN)

    times = inputNumberSafely("How many to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        print(f"Profile {i}:")
        for property, value in randomGenerator.full_profiles()[0].items():
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

def coinFlipMenu():
    """ Coin flip generator. """
    print(end=Fore.GREEN)

    times = inputNumberSafely("How many to generate?: ", canNegative=False)
    for i in range(1, times + 1):
        flip = random.choice(["heads", "tails"])
        print(f"Flip {i}: {flip}")

def randomNumberMenu():
    """ Random number generator. """
    print(end=Fore.GREEN)

    start = inputNumberSafely("What is the minimum number to generate? (inclusive): ")
    end   = inputNumberSafely("What is the maximum number to generate? (inclusive): ")

    if start > end:
        print(end=Fore.RED)
        print(f"Invalid range ({start}-{end})! The minimum cannot be larger than the maximum")
        return

    times = inputNumberSafely("How many to generate?: ", canNegative=False)

    for i in range(1, times + 1):
        number = random.randint(start, end)
        print(f"Number {i}: {number}")



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
        print("(1) Name gen        (2) Address gen      ".center(lineLength))
        print("(3) Password gen    (4) Email gen        ".center(lineLength))
        print("(5) Profile gen     (6) Coordinate gen   ".center(lineLength))
        print("(7) Coin flip gen   (8) Random number gen".center(lineLength))
        print("(9) Exit                                 ".center(lineLength))
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
                printTitle("(USA) ADDRESS GENERATOR")
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
            elif sanatizedOption == '7':
                printTitle("COIN FLIP GENERATOR")
                loopUntilStopped(coinFlipMenu)
            elif sanatizedOption == '8':
                printTitle("RANDOM NUMBER GENERATOR")
                loopUntilStopped(randomNumberMenu)
            elif sanatizedOption != '9':
                # No need to print an error if they typed nothing.
                if sanatizedOption:
                    print(end=Fore.RED); print(f"Invalid option '{option}'!")
                continue

            break

        if sanatizedOption == '9':
            break

if __name__ == '__main__':
    main()
