#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

# import local module for welcome message
import stringer

NAME = "My 3 Test Scores"
AUTHOR = "Erin"

def main():
    stringer.show_welcome(NAME)
    should_Exit = False
    
    while not should_Exit:
        total_score = score1 = score2 = score3 = 0
        print()
        
        #get scores from the user
        try:
            score1 = int(input("Enter first test score: "))
        except ValueError:
            print ("ERROR, test score MUST be a number!")
            continue
        if score1 < 0 or score1 > 100:
            print ("ERROR, test score MUST be a number between 0-100")
            continue
        total_score += score1
        try:
            score2 = int(input("Enter second test score: "))
        except ValueError:
            print ("ERROR, test score MUST be a number between 0-100")
            continue
        if score2 < 0 or score2 > 100:
            print ("ERROR, test score MUST be a number between 0-100")
            continue
        total_score += score2
        try:
            score3 = int(input("Enter third test score: "))
        except ValueError:
            print ("ERROR, test score MUST be a number between 0-100")
            continue
        if score3 < 0 or score3 > 100:
            print ("ERROR, test score MUST be a number between 0-100")
            continue

        total_score += score3

        # calculate average score
        average_score = round(total_score / 3)
             
        # format and display the result
        print("======================")
        print("Your scores:\t",score1,score2,score3)
        print("Total Score:  ", total_score,
            "\nAverage Score:", average_score)
        print()
        if average_score > 89:
            print ("Congratulations!!! You are an 'A' student!!!")
        elif average_score > 79:
            print ("Congratulations!! You are a 'B' student!!")
        elif average_score > 69:
            print ("Congratulations! You are a 'C' student.")
        elif average_score > 59:
            print ("Congratulations. You are still a student.")
        else:
            print ("You should find vocational work!!!!")
        choice = input("Try again? (y/n): ")
        if choice.lower() != "y":
            should_Exit = True
        # end while loop
    print("Bye!")
# end main

#if the current module is the main module
if __name__ == "__main__":
  main()
