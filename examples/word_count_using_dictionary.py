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

import os.path
import codecs

AUTHOR = "Erin Coffey"
NAME = "Use a dictionary to count words"

def read_file(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as f:
            text = f.read()          # caution, we are reading the whole file
        text = text.replace("\n", "")
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.lower()
        f.close()
    except Exception as e:
        raise e

    words = text.split(" ")         # split on space and convert str to list
    return words

# end read_file()

def display_menu():
    print()
    print("COMMAND MENU")
    print("exit - Exit program")

# end display_menu()

def get_words(file):
    words = []
    choice = "y"
    try:
        if os.path.isfile(file):
            # the file is where we expected it
            # check the size and warn the user a large file might take a long time to process!
            info = os.stat(file)
            size = info.st_size
            mbSize = round(size/1048576, 2)
            if mbSize > 1:
                print("The size of the file is " + str(mbSize) + " MB")
                choice = input("Are you sure you want to continue with such a large file? (y/n)")
                choice = choice.lower()
            if choice == "y":
                words = read_file(file)
            else:
                words = ["big", "file"]
        else:
            # the file does not exist where it is expected
            # initialize data and try to create the file
            raise Exception("File not found.")
    except Exception as e:
        raise e
    
    return words

# end get_words()

def count_words(words):
    word_count = {}                                 # create the dictionary to make counting words efficient
    for word in words:
        word = word.strip()
        if word in word_count:
            word_count[word] += 1                   # increment the counter forn this word
        else:
            word_count[word] = 1                    # add the new word and set count to 1
    return word_count

# end count_words()

def display_word_count(word_count):
    words = list(word_count.keys())                 # make a list of the keys
    words.sort(key=str.lower)                       # sort alphbetically
    for word in words:
        count = word_count[word]                    # get the value from the key
        print(word, "=", count)

# end display_word_count()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    display_menu()
    print()

    while True:
        print()
        file = input("Path to .txt file? ")
        print()
        try:
            if file == "exit":
                break
            else:
                words = get_words(file)             # get a list of words from the file
                word_count = count_words(words)     # create a dictionary
                display_word_count(word_count)
                
        except Exception as e:
            print("There was an Error processing your file.", e)
            continue

    # end while loop
        
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
