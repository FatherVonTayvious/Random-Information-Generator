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

print(Fore.RED + "[------------------------------------------]")
print(Fore.CYAN + "        ______    _   _               ")
print(Fore.CYAN + "       |  ____|  | | | |              ")
print(Fore.CYAN + "       | |__ __ _| |_| |__   ___ _ __ ")
print(Fore.CYAN + "       |  __/ _` | __| '_ \ / _ \ '__|")
print(Fore.CYAN + "       | | | (_| | |_| | | |  __/ |   ")
print(Fore.CYAN + "       |_|  \__,_|\__|_| |_|\___|_|   ")
print(Fore.GREEN + "  Welcome to Random Information Generation")
print(Fore.RED + "[------------------------------------------]")
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
        print(Fore.RED + "[------------------------------------------]")
        print(Fore.CYAN + "        ______    _   _               ")
        print(Fore.CYAN + "       |  ____|  | | | |              ")
        print(Fore.CYAN + "       | |__ __ _| |_| |__   ___ _ __ ")
        print(Fore.CYAN + "       |  __/ _` | __| '_ \ / _ \ '__|")
        print(Fore.CYAN + "       | | | (_| | |_| | | |  __/ |   ")
        print(Fore.CYAN + "       |_|  \__,_|\__|_| |_|\___|_|   ")
        print(Fore.GREEN + "             NAME GENERATOR")
        print(Fore.RED + "[------------------------------------------]")
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
        print(Fore.RED + "[------------------------------------------]")
        print(Fore.CYAN + "        ______    _   _               ")
        print(Fore.CYAN + "       |  ____|  | | | |              ")
        print(Fore.CYAN + "       | |__ __ _| |_| |__   ___ _ __ ")
        print(Fore.CYAN + "       |  __/ _` | __| '_ \ / _ \ '__|")
        print(Fore.CYAN + "       | | | (_| | |_| | | |  __/ |   ")
        print(Fore.CYAN + "       |_|  \__,_|\__|_| |_|\___|_|   ")
        print(Fore.GREEN + "           ADDRESS GENERATOR")
        print(Fore.RED + "[------------------------------------------]")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")

        state = input("State (CA CT VT AL AR DC FL GA KY TN MD OK TX): ")

        print(random_address.real_random_address_by_state(state))
    address()

if option == "3":
    def both():
        print(Fore.RED + "[------------------------------------------]")
        print(Fore.CYAN + "        ______    _   _               ")
        print(Fore.CYAN + "       |  ____|  | | | |              ")
        print(Fore.CYAN + "       | |__ __ _| |_| |__   ___ _ __ ")
        print(Fore.CYAN + "       |  __/ _` | __| '_ \ / _ \ '__|")
        print(Fore.CYAN + "       | | | (_| | |_| | | |  __/ |   ")
        print(Fore.CYAN + "       |_|  \__,_|\__|_| |_|\___|_|   ")
        print(Fore.GREEN + "           Name+Address Gen")
        print(Fore.RED + "[------------------------------------------]")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")

        print("Name: " + names.get_full_name())
        print("Address: ")
        print(random_address.real_random_address_by_state('CA'))
    both()
if option == "4":
    def random_char(y):
        print(Fore.RED + "[------------------------------------------]")
        print(Fore.CYAN + "        ______    _   _               ")
        print(Fore.CYAN + "       |  ____|  | | | |              ")
        print(Fore.CYAN + "       | |__ __ _| |_| |__   ___ _ __ ")
        print(Fore.CYAN + "       |  __/ _` | __| '_ \ / _ \ '__|")
        print(Fore.CYAN + "       | | | (_| | |_| | | |  __/ |   ")
        print(Fore.CYAN + "       |_|  \__,_|\__|_| |_|\___|_|   ")
        print(Fore.GREEN + "           GMAIL GENERATOR")
        print(Fore.RED + "[------------------------------------------]")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")
        return ''.join(random.choice(string.ascii_letters) for x in range(y))


    print(random_char(7) + "@gmail.com")
    gmail()

if option == "5":
    def profile():
        print(Fore.RED + "[------------------------------------------]")
        print(Fore.CYAN + "        ______    _   _               ")
        print(Fore.CYAN + "       |  ____|  | | | |              ")
        print(Fore.CYAN + "       | |__ __ _| |_| |__   ___ _ __ ")
        print(Fore.CYAN + "       |  __/ _` | __| '_ \ / _ \ '__|")
        print(Fore.CYAN + "       | | | (_| | |_| | | |  __/ |   ")
        print(Fore.CYAN + "       |_|  \__,_|\__|_| |_|\___|_|   ")
        print(Fore.GREEN + "           PROFILE GENERATOR")
        print(Fore.RED + "[------------------------------------------]")
        print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
        print(Fore.RED + "[------------------------------------------]")
        print("Profile : ")
        print(rp.full_profile())
    profile()
