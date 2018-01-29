#!/usr/bin/env python3

# an example Python program working with dictionaries
# by Erin Coffey
# 29 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import local module for welcome message
import stringer
# import module for tracking lost time
import timer

AUTHOR = "Erin Coffey"
NAME = "Store Country codes in a dictionary"


def display_menu():
    print("COMMAND MENU")
    print("view - View country name")
    print("add  - Add a country")
    print("del  - Delete a country")
    print("help - See this menu")
    print("exit - Exit program")

# end display_menu()

def display_codes(countries):
    # make a list of the keys
    codes = list(countries.keys())
    # sort the list
    codes.sort()
    line = "Current country codes: "
    print()
    for code in codes:
        line += code + " "
    print(line)

# end display_codes()

def view(countries):
    display_codes(countries)
    code = input("Enter Country code: ")
    code = code.upper()
    print()
    if code in countries:
        name = countries[code]
        print("Country name: " + name)
    else:
        print("The code " + code + " was not found.")

# end view()

def add(countries):
    code = input("Enter new country code: ")
    code = code.upper()
    print()
    if code in countries:
        print("The code " + code + " is already in the database.")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(name + " was added.")

# end add()

def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    print()
    if code in countries:
        name = countries.pop()
        print(name + " was deleted.")
    else:
        print("The code " + code + " was not found.")

# end delete()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)

    countries = {"CA": "Canada",
                 "US": "United States",
                 "MX": "Mexico"}
    
    display_menu()

    while True:
        print()
        command = input("By your command: ")
        print()
        try:
            command = command.lower().strip()
            if command == "view":
                view(countries)
            elif command == "add":
                add(countries)
            elif command == "del":
                delete(countries)
            elif command == "h" or command == "help":
                display_menu()
            elif command == "exit":
                break
            else:
                print(command + " is not a valid command. Please try again.")
                continue

        except Exception as e:
            print("There was an Error processing your command: ", e)
            continue

    # end while loop
        
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()

