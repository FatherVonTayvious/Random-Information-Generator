import time

import random_address
from random_address import real_random_address
import names
from colorama import Fore, Back, Style
import random
import random
import string
from random_profile import RandomProfile
rp = RandomProfile(num=1)
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

def printTitle(title: str):
    """ Prints the logo with a section title embedded inside. """
    print(Fore.RED + "[{}]".format('-' * (lineLength-2)))
    for line in logoASCII:
        print(Fore.CYAN + line.center(lineLength))
    print(Fore.GREEN + title.center(lineLength))
    print(Fore.RED + "[{}]".format('-' * (lineLength-2)))


printTitle("Welcome to Random Information Generation")
print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
print(Fore.RED + "[------------------------------------------]")
print(Fore.RED + "              Content Table")
print(Fore.RED + " (1) Name Generator    (2) Address generator")
print(Fore.RED + " (3) Name+Address       (4) Gmail generator")
print(Fore.RED + "           (5) Profile Generator")
print(Fore.RED + "[------------------------------------------]")

option = input(Fore.GREEN + "Option: ")

if option == "1":
    def name():
        printTitle("NAME GENERATOR")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")

        opt2 = input("Full,First or Last: ")

        if opt2.lower() in ['Full', 'full']:
            print("Name: " + names.get_full_name())
        else:
            if opt2.lower() in ['First', 'first']:
                print("Name: " + names.get_first_name())
            else:
                if opt2.lower() in ['Last', 'last']:
                    print("Name: " + names.get_first_name())
                    time.sleep(2)
                    _0x47 = input("Would you like to exit? [Y/N]: ")
                    if _0x47 == "Y":
                        return
                    elif _0x47 == "N":
                        return name()
    name()

if option == "2":
    def address():
        printTitle("ADDRESS GENERATOR")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")

        state = input("State (CA CT VT AL AR DC FL GA KY TN MD OK TX): ")

        print(random_address.real_random_address_by_state(state))
    address()

if option == "3":
    def both():
        printTitle("Name+Address Gen")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")

        print("Name: " + names.get_full_name())
        print("Address: ")
        print(random_address.real_random_address_by_state('CA'))
    both()
if option == "4":
    def random_char(y):
        printTitle("GMAIL GENERATOR")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")
        return ''.join(random.choice(string.ascii_letters) for x in range(y))


    print(random_char(7) + "@gmail.com")

if option == "5":
    def profile():
        printTitle("PROFILE GENERATOR")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")
        print("Profile : ")
        print(rp.full_profile())
    profile()
