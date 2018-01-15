#!/usr/bin/env python3

# an example Python program with imported random module
# by Erin Coffey
# 12 January 2018

# import the random module
import random
# import local module for welcome message
import stringer

AUTHOR = "Erin"
NAME = "Number Guessing Game"
LIMIT = 10

def play_game():
    number = random.randint(1, LIMIT)
    print("\nI'm thinking of a number from 1 to " + str(LIMIT) + "\n")
    tries = 1
    while True:
        try:
            guess = int(input("What is your guess? "))
        except ValueError:
            print ("ERROR, your guess MUST be a number. Please try again.")
            continue
        if guess < number:
            print("Too low!")
            tries += 1
        elif guess > number:
            print("Too high!")
            tries += 1
        else:
            if tries > 1:
                print("You guessed my number in " + str(tries) + " tries!")
            else:
                print("Genius!! You guessed my number in " + str(tries) + " try!")
            return
# end play_game()

def main():
    stringer.show_welcome(NAME)
    should_Exit = False
    converted_temp = 0.0
    while not should_Exit:
        play_game()
    
        choice = input("Go again? (y/n): ")
        if choice.lower() != "y":
            should_Exit = True
    # end while loop
    print("Bye!")
# end main()

#if the current module is the main module
if __name__ == "__main__":
  main()
