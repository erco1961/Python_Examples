#!/usr/bin/env python3

# an example Python program with imported modules
# by Erin Coffey
# 12 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import the Temp class from the temperature module
from temperature import Temp
# import stringer module for welcome message
import stringer
# import module for tracking lost time
import timer

NAME = "Temperature Converter"
AUTHOR = "Erin Coffey"

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    converted_temp = 0.0
    while True:
        converter = Temp()          # create instance of Temp class obj
        print()
        # get input from the user
        scale = input("Enter current scale \'F\' or \'C\':\t")
        if scale.lower() != 'c' and scale.lower() != 'f':
            print ("ERROR, invalid scale. Please try again.")
            continue
        try:
            temperature = float(input("Enter current temperature:\t"))
        except ValueError:
            print ("ERROR, temperature should be a number. Please try again.")
            continue

        if scale.lower() == 'f':
            converted_temp = converter.getCelsius(temperature)
            print("Degrees Celsisus = ",end=" ")
        else:
            converted_temp = converter.getFahrenheit(temperature)
            print("Degrees Fahrenheit = ",end=" ")
            
        print(str(converted_temp))
    
        choice = input("Go again? (y/n): ")
        if choice.lower() != "y":
            break
    # end while loop
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()

#if the current module is the main module
if __name__ == "__main__":
  main()
