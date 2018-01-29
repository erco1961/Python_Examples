#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import local module for welcome message
import stringer
# import module for tracking lost time
import timer

NAME = "Rectangle Area and Perimiter"
AUTHOR = "Erin Coffey"

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    should_Exit = False
    
    while not should_Exit:
        print()

        # get input from the user
        length = float(input("Enter Rectangle length:\t"))
        width = float(input("Enter Rectangle width:\t"))

        # calculate 
        area = round(length * width,2)
        perimiter = round(length * 2 + width * 2,2)

        print()
        print("Area =\t\t",area)
        print("Perimiter =\t",perimiter)
        print()

        choice = input("Try again? (y/n): ")
        if choice.lower() != "y":
            should_Exit = True
    # end while loop
    timer.stop_timer(myTimer)
    print("Bye!")
# end main

#if the current module is the main module
if __name__ == "__main__":
  main()

