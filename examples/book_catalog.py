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
NAME = "Use dictionary for book catalog"

def display_menu():
    print("COMMAND MENU")
    print("show - Show book info")
    print("add  - Add a book")
    print("del  - Delete a book")
    print("edit - Edit book info")
    print("help - See this menu")
    print("exit - Exit program")

# end display_menu()

def show_book(catalog):
    title = input("Enter book title: ")
    if title in catalog:
        book = catalog[title]
        print("Title:               " + title)
        print("Author:              " + book["author"])       
        print("Publication year:    " + book["pubYear"])
    else:
        print("\"" + title + "\" was not found in the catalog.")
# end show_book()

def add_edit_book(catalog, mode):
    title = input("Enter book title: ")
    if mode == add and title in catalog:
        print("\"" + title + " is already in the catalog.")
        response = input("Would you like to edit it? (y/n): ").lower()
        if response != "y":
            return
    elif mode == edit and title not in catalog:
        print("\"" + title + "\" was not found in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if response != "y":
            return

    # create the new entry
    author = input("Enter Author name: ")
    pubYear = input("Enter publication year: ")
    book = {"author": author, "pubYear": pubYear}
    catalog[title] = book
# end add_edit_book()

def delete_book(catalog):
    title = input("Enter book title: ")
    if title in catalog:
        del catalog[title]
        print("\"" + title + " was removed.")
    else:
        print("\"" + title + "\" was not found in the catalog.")

# end delete_book()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)

    catalog = {
        "Moby Dick":
            {"author" : "Herman Melville",
             "pubYear" : "1851"},
        "The Hobbit":
            {"author" : "J. R. R. Tolkien",
             "pubYear" : "1937"}
        }
    
    display_menu()

    while True:
        print()
        command = input("By your command: ")
        print()
        try:
            command = command.lower().strip()
            if command == "show":
                show_book(catalog)
            elif command == "add" or command == "eidt":
                add_edit_book(catalog, mode=command)
            elif command == "del":
                delete_book(catalog)
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
