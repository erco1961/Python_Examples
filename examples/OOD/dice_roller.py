#!/usr/bin/env python3

# an example Python program working with dictionaries
# by Erin Coffey
# 29 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules2/"
sys.path.append(MODULES_DIR)
# import local module for welcome message
import stringer
# import module for tracking lost time
import timer

from dice import Dice, Die
import validation as val

AUTHOR = "Erin Coffey"
NAME = "Composit Object Oriented Dice Roller"

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    print()

    while True:
        print()
        
        try:
            number = val.get_int("Enter number of dice to roll: ",10,0)# use validation module to set max 10 dice

            #create Dice object to hold the dice
            dice = Dice()
            for i in range(number):
                die = Die()
                dice.addDie(die)

            #roll dem bones!
            dice.rollAll()

            print("YOUR ROLL: ")
            # use itertor from class Dice
            for die in dice:
                print(die.getImage())               
            print()
                
        except Exception as e:
            print("There was an Error processing your roll.", e)
            break

        choice = input("Roll again? (y/n): ").lower()
        if choice != "y":
            break

    # end while loop
        
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
