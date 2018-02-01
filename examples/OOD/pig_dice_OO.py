#!/usr/bin/env python3

# an example Python program using object composition and encapsulation
# by Erin Coffey
# 01 February 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import local module for welcome message
import stringer
# import random for dice rolls
import random
# import module for tracking lost time
import timer

from objects import Game

NAME = "Object Oriented Pig Dice"
AUTHOR = "Erin Coffey"

def display_rules():
    print("\nHow to play the PIG game...")
    print()
    print("* See how many turns it takes to score 20 points.")
    print("* A turn ends when you HOLD or, roll a '1'")
    print("* If you roll a '1', you lose ALL points for the turn.")
    print("* If you HOLD, you save all points for the turn.")
    print()
    print("* You can EXIT by typing exit")
# end display_rules

def take_turn(game):
    print("TURN:\t", str(game.turn))
    game.scoreThisTurn = 0
    game.isTurnOver = False

    while not game.isTurnOver:
        choice = input("Roll or Hold? (r/h): ")
        if choice.lower() == "r":
            roll_die(game)
        elif choice.lower() == "h":
            hold_turn(game)
        elif choice.lower() == "exit":
            game.isGameOver = True
            game.isTurnOver = True
        else:
            print("Invalid selection. Please try again.")
# end take_turn

def roll_die(game):
    game.die.roll()
    print(game.die.getImage())
    if game.die.value == 1:
        game.score_this_turn = 0
        game.turn += 1
        print("Turn over. No score for you!\n")
        game.isTurnOver = True
    else:
        game.scoreThisTurn += game.die.value
# end roll_die

def hold_turn(game):
    print("Score for turn:\t" + str(game.scoreThisTurn))
    game.score += game.scoreThisTurn
    print("Total Score:\t", game.score)
    game.isTurnOver = True
    if game.score >= 20:
        print("You completed the game in "+ str(game.turn) + " turn", end = "")
        game.isOver = True
        if game.turn > 1:
            print("s.")
        else:
            print("!!!")# get really excited if only one turn to win
        game.isGameOver = True
    else:
        game.turn += 1
# end hold_turn

def play_game():
    game = Game()
    while not game.isGameOver:
        take_turn(game)
    print()
    print("Game over!")
# end play_game

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    display_rules()
    should_Exit = False
    
    while not should_Exit:
        print()
        play_game()

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

