#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

# import local module for welcome message
import stringer
# import module for tracking lost time
import timer

NAME = "Miles per Gallon"
AUTHOR = "Erin Coffey"

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    miles_driven = gallons_used = cost_per_gallon = 0
    should_Exit = False
    while not should_Exit:
        print()
    #   get input from the user
        try:
            miles_driven = float(input("Enter miles drivens:\t\t"))
            gallons_used = float(input("Enter gallons of gas used:\t"))
            cost_per_gallon = float(input("Enter cost per gallon:\t\t"))
        except ValueError:
            print ("ERROR, ALL values entered must belong to the set containing only numbers. Please try again.")
            continue

        if miles_driven <= 0.0:
            print ("Miles driven must be greater than zero! Please try again.")
            continue
        elif gallons_used <= 0.0:
            print ("Gallons used must be greater than zero! Please try again.")
            continue
        elif cost_per_gallon <= 0.0:
            print ("Cost per gallon must be greater than zero! Please try again.")
            continue

    #   calculate miles per gallon
        mpg = miles_driven / gallons_used
        mpg = round(mpg, 2)

    #   calculate total cost of gas
        total_cost = round(gallons_used * cost_per_gallon,2)

    #   calculate cost per mile
        cost_per_mile = round(total_cost / miles_driven,2)
            
    #   format and display the result
        print()
        print("Miles Per Gallon:\t\t" + str(mpg))
        print("Total gas cost:\t\t\t" + str(total_cost))
        print("Cost per mile:\t\t\t" + str(cost_per_mile))
        print()
        choice = input("Try again? (y/n): ")
        if choice.lower() != "y":
            should_Exit = True
    #   end while loop
    timer.stop_timer(myTimer)
    print("Bye!")
# end main


#if the current module is the main module
if __name__ == "__main__":
  main()

