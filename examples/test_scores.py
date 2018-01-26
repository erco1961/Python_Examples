#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

# import local module for welcome message
import stringer
# import module for tracking lost time
import timer

NAME = "Test Scores"
AUTHOR = "Erin Coffey"


def display_help():
    print("Enter 'x' to exit")

# end display_help

def get_score():
    while True:
        score = input("Enter test score: ")
        if score.lower() == "x":
            return score
        else:
            try:
                score = int(score)
            except ValueError:
                print ("ERROR, Score must be an integer number. Please try again.")
                continue
        if score < 0 or score > 100:
            print ("ERROR, Score must be greater than 0 and, less than 100. Please try again.")
            continue
        else:
            return score

# end get_score()

def get_scores(scores):
    while True:
        score = get_score()
        if score != "x":
            scores.append(score)
        else:
            break
    if len(scores) > 0:
        return 1
    else:
        return "x"

# end get_scores()

def calculate_total_score(scores):
    total = 0
    for score in scores:
        total += score
    return total

# end calculate_total_score()

def display_results(scores):
    scores.sort()
    # get med index by divide and truncate
    median_index = len(scores) // 2
    median_value = scores[median_index]
    
    total_score = calculate_total_score(scores)
    # calculate average score
    average_score = round(total_score / len(scores))

    # format and display the result
    print("======================")
    print("Total Score:      ", total_score,
          "\nNumber of Scores: ", len(scores),
          "\nAverage Score:    ", average_score,
          "\nLow Score:        ", min(scores),
          "\nHigh Score:       ", max(scores),
          "\nMedian Score:     ", median_value)
          
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
        print ("Perhaps, you should find vocational work.")

# end display_results()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    display_help()
    
    while True:
        scores = []
        response = get_scores(scores)
        if response != "x":
            display_results(scores)
        print()
    

        choice = input("Try again? (y/n): ")
        if choice.lower() != "y":
            break
        # end while loop
    timer.stop_timer(myTimer)
    print("Bye!")
# end main

#if the current module is the main module
if __name__ == "__main__":
  main()
