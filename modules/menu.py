# This file contains the functions used to create and access the menu in the main program

selection = "0"


def main():
    print("1) Start Chatting!")
    print("2) Access RandomStuff text file")
    print("E) Exit")
    global selection
    selection = input("Please choose an option from the menu: ")


main()
print(selection)
