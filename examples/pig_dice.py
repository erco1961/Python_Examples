#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

# import local module for welcome message
import stringer
# import random for dice rolls
import random

NAME = "Pig Dice"
AUTHOR = "Erin Coffey"

def display_rules():
    print("\nHow to play the PIG game...")
    print()
    print("* See how many turns it takes to score 20 points.")
    print("* A turn ends when you HOLD or, roll a '1'")
    print("* If you roll a '1', you lose ALL points for the turn.")
    print("* If you HOLD, you save all points for the turn.")
    print()
# end display_rules

def take_turn(turn, score, game_over):
    print("TURN:\t", str(turn))
    score_this_turn = 0
    turn_over = False

    while not turn_over:
        choice = input("Roll or Hold? (r/h): ")
        if choice.lower() == "r":
            turn, score, score_this_turn, turn_over = \
              roll_die(turn, score, score_this_turn)
        elif choice.lower() == "h":
            turn, score, turn_over, game_over = \
              hold_turn(turn, score, score_this_turn)
        else:
            print("Invalid selection. Please try again.")
    return turn, score, game_over
# end take_turn

def roll_die(turn, score, score_this_turn):
    die = random.randint(1,6)
    print("DIE:\t" + str(die))
    if die == 1:
        score_this_turn = 0
        turn += 1
        print("Turn over. No score for you!\n")
        turn_over = True
    else:
        score_this_turn += die
        turn_over = False
    return turn, score, score_this_turn, turn_over
# end roll_die

def hold_turn(turn, score, score_this_turn):
    print("Score for turn:\t" + str(score_this_turn))
    score += score_this_turn
    print("Total Score:\t" + str(score))
    turn_over = True
    game_over = False
    if score >= 20:
        print("You completed the game in "+ str(turn) + " turn", end = "")
        if turn > 1:
            print("s.")
        else:
            print("!!!")
        game_over = True
        return turn, score, turn_over, game_over
    turn += 1
    return turn, score, turn_over, game_over
# end hold_turn

def play_game():
    game_over = False
    turn = 1
    score = 0
    while not game_over:
        turn, score, game_over = take_turn(turn, score, game_over)
    print()
    print("Game over!")
# end play_game

def main():
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
    print("Bye!")
# end main


#if the current module is the main module
if __name__ == "__main__":
  main()

