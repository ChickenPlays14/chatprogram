# import random
import time
# import ranquestions.py
import modules.menu


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


selection = None

while selection != "E":
    modules.menu.main()

    selection = input("Please choose an option from the menu: ")

    if selection == "2":
        while selection != "B":
            modules.menu.randomstuff()
            selection = input("Please choose an option from the menu: ")
            if selection == "1":
                file = open("randomstuff.txt", "a")
                ranstwrite = input("Enter anything you want! ")
                file.write(ranstwrite + "\n")
                print(bcolors.OKGREEN + "Saved!" + bcolors.ENDC)
                file.close()
                time.sleep(2)

            elif selection == "2":
                file = open("randomstuff.txt", "r")
                print(file.read())
                file.close()
                time.sleep(2)
