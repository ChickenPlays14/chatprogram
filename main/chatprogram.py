# import random
import time
# import ranquestions.py
import modules.menu

selection = None

while selection != "E":
    modules.menu.main()

    selection = input("Please choose an option from the menu: ")

    if selection == "2":
        while selection != "E":
            modules.menu.randomstuff()
            selection = input("Please choose an option from the menu: ")
            if selection == "1":
                file = open("randomstuff.txt", "a")
                ranstwrite = input("Enter anything you want! ")
                file.write(ranstwrite + "\n")
                file.close()
