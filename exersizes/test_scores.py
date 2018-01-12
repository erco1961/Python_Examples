#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

import sys

# display a welcome message
print("***************** PYTHON ******************")
print("**  Erin\'s Test Score Averaging program  **")
print("***************** PYTHON ******************")
print()

print("Enter a test score")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score1 = 0
score2 = 0
score3 = 0
try:
    score1 = int(input("Enter first test score: "))
except ValueError:
    print ("ERROR, test score MUST be a number!")
    sys.exit()
if score1 < 0 or score1 > 100:
    print ("ERROR, test score MUST be a number between 0-100")
    sys.exit()
total_score += score1
try:
    score2 = int(input("Enter second test score: "))
except ValueError:
    print ("ERROR, test score MUST be a number between 0-100")
    sys.exit()
if score2 < 0 or score2 > 100:
    print ("ERROR, test score MUST be a number between 0-100")
    sys.exit()
total_score += score2
try:
    score3 = int(input("Enter third test score: "))
except ValueError:
    print ("ERROR, test score MUST be a number between 0-100")
    sys.exit()
if score3 < 0 or score3 > 100:
    print ("ERROR, test score MUST be a number between 0-100")
    sys.exit()

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
print("Bye")


