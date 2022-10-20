import time
import random_address
import names
from colorama import Fore, Style
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

def printSeparator():
    """ Prints the separator bar used throughout the user interface. """
    print(Fore.RED + "[{}]".format('-' * (lineLength-2)))

def printTitle(title: str):
    """ Prints the logo with a section title embedded inside. """
    printSeparator()
    for line in logoASCII:
        print(Fore.CYAN + line.center(lineLength))
    print(Fore.GREEN + title.center(lineLength))
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



def getName():
    """ Name generator. """
    while True:
        printTitle("NAME GENERATOR")
        print(Style.BRIGHT + Fore.YELLOW + "Tool made by Father VonTayvious#0001".center(lineLength))
        printSeparator()

        choice = input("Full, First, or Last: ")
        sanatizedChoice = choice.lower()

        if sanatizedChoice == "full":
            print("Name: " + names.get_full_name())
        elif sanatizedChoice == "first":
            print("Name: " + names.get_first_name())
        elif sanatizedChoice == 'last':
            print("Name: " + names.get_first_name())
        else:
            print(f"Invalid option '{choice}'!")
            continue
            
        time.sleep(2)
        if not askToContinue():
            break
                
def getAddress():
    """ Address generator. """
    printTitle("ADDRESS GENERATOR")
    print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
    printSeparator()

    state = input("State (CA CT VT AL AR DC FL GA KY TN MD OK TX): ")

    print(random_address.real_random_address_by_state(state))

def getNameAddress():
    """ Name and address generator. """
    printTitle("Name+Address Gen")
    print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
    printSeparator()

    print("Name: " + names.get_full_name())
    print("Address: ")
    print(random_address.real_random_address_by_state('CA'))
    
def getGmail():
    """ Gmail generator. """
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    printTitle("GMAIL GENERATOR")
    print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
    printSeparator()
    print(random_char(7) + "@gmail.com")

def getProfile():
    """ Profile generator. """
    printTitle("PROFILE GENERATOR")
    print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
    printSeparator()
    print("Profile : ")
    for property, value in rp.full_profile()[0].items():
        print("\t{}: {}".format(property, value))



def main():
    printTitle("Welcome to Random Information Generation")
    print(Style.BRIGHT + Fore.YELLOW + "    Tool made by Father VonTayvious#0001")
    printSeparator()
    print(Fore.RED + "              Content Table")
    print(Fore.RED + " (1) Name Generator    (2) Address generator")
    print(Fore.RED + " (3) Name+Address       (4) Gmail generator")
    print(Fore.RED + "           (5) Profile Generator")
    printSeparator()

    option = input(Fore.GREEN + "Option: ")

    if option == '1':
        getName()
    elif option == '2':
        getAddress()
    elif option == '3':
        getNameAddress()
    elif option == '4':
        getGmail()
    elif option == '5':
        getProfile()
    else:
        print(f"Invalid option '{option}'!")

if __name__ == '__main__':
    main()