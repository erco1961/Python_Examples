#!/usr/bin/env python3

# an example Python program working with string credentials as user input
# by Erin Coffey
# 24 January 2018

# import local module for welcome message
import stringer
# import module for tracking lost time
import timer
#hide user input while entering password
import getpass
import sys

AUTHOR = "Erin Coffey"
NAME = "Validating user credentils as String input"

def get_full_name():
    while True:
        name = input("Enter First and Last name:       ").strip()
        if " " in name:
            return name.title()
        else:
            print("You must enter your First and Last name. Please try again.")

# end get_full_name()

def get_password():
    while True:
        if sys.stdin.isatty():
            password = getpass.getpass("Enter password:       ")
        else:
            password = sys.stdin.readline().rstrip()
        digits = False
        caps = False
        for char in password:
            if char.isdigit():
                digits = True
            elif char.isupper():
                caps = True
        if digits == False or caps == False or len(password) < 8:
            print("Password must be at least 8 characters long and" +
                  " must have at least one digit and one uppercase letter.\n"+
                  "Please try again.")
            continue
        else:
            return password

# end get_password()

def get_first_name(full_name):
    index = full_name.find(" ")
    first_name = full_name[:index]# everything before the space
    return first_name
        
# end get_first_name()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)

    while True:
        print()
        full_name = get_full_name()

        password = get_password()

        first_name = get_first_name(full_name)

        print("Hi " + first_name + " thanks for creating an account.")

        choice = input("Try \'" + NAME + "\' program again? (y/n): ")
        if choice.lower() != "y":
          break
    # end while loop
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
