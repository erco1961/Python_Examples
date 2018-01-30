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
# import module for limiting the size of integer input
import validation as val

AUTHOR = "Erin Coffey"
NAME = "Use recursion to calculate factorial"

def display_menu():
    print()
    print("COMMAND MENU")
    print("fib    - Displays fibonacci series")
    print("fac    - Calculates factorial")
    print("exit   - Exit program")
    print("help   - Shows this menu")

# end display_menu()

def display_warning():
    print()
    print("WARNING: This program uses recursion...\n")
    print("If you input a large number, you may exceed your system's stack!")
    print()

# end display_menu()

def calculate_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)
    
# end calculate_factorial()

def my_factorial():
    num = val.get_int("Enter an integer number less than 15: ", 15)
    print()
    try:
        result = calculate_factorial(num)
        print("The factorial value of " + str(num) + " is: " + str(result))
                
    except Exception as e:
        print("There was an Error processing your number.", e)

# end my_factorial()

def calculate_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return calculate_fib(num - 1) + calculate_fib(num - 2)
        

# end calculate_fib()

def my_fib():
    num = val.get_int("Enter an integer number less than 25: ", 25)
    print()
    try:
        for i in range(num):
            print(calculate_fib(i), end=" ")
                
    except Exception as e:
        print("There was an Error processing your number.", e)

# end my_fib()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    display_warning()
    print()
    display_menu()

    while True:
        print()
        command = input("\nBy Your Command...\t")
        command = command.rstrip()
        if command.lower() == "fac":
            my_factorial()
        elif command.lower() == "fib":
            my_fib()
        elif command.lower() == "help":
            display_menu()
        elif command.lower() == "exit":
            break
        else:
            print("\""+ str(command) + "\" is not a valid selection. Please try again.\n")

    # end while loop
        
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
