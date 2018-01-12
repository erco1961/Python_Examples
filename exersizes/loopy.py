#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 11 January 2018

import sys

# display a welcome message
print("*************** PYTHON ****************")
print("**  Erin\'s Looping examples program  **")
print("*************** PYTHON ****************")

num_Loops = 0
should_Exit = False
while not should_Exit:
 print()
# get input from the user
 try:
    num_Loops = int(input("Enter number of times to loop: "))
 except ValueError:
    print ("ERROR, number of times to loop should be an integer. Please try again.")
    continue

 if num_Loops <= 0.0:
    print ("Number of times to loop must be greater than zero! Please try again.")
    continue
 elif num_Loops > 10.0:
    print (str(num_Loops) + " times to loop is too ambitious! Automatically re-setting to 10.")
    num_Loops = 10

# loop specified number of times
 total = 0
 final = num_Loops - 1
 print()
 print("Looping through range from 0 to " + str(final))
 for i in range(num_Loops):
     total += i
     print(i, end = " ")

 print()
 print("Looping backwards through range from " + str(num_Loops) + " down to 1") 
 for i in range(num_Loops, 0, -1):
     print(i, end = " ")
 print()
 print("Looping through range from 0 to " + str(num_Loops) + " by 2s") 
 for i in range(2, num_Loops+1, 2):
     print(i, end = " ")
 print()
 print("The sum of the numbers from 0 to " + str(final) + " is: " + str(total))         
 print()
 choice = input("Want to know how much a $10,000 investment at 5% interest will be worth in " + str(num_Loops) + " years? (y/n): ")
 if choice.lower() != "y":
     break
 investment = 10000
 for i in range(num_Loops):
     yearly_interest = investment * .05
     investment = investment + yearly_interest
 investment = round(investment, 2)
 print("After " + str(num_Loops) + " years, your $10,000 investment is now worth $" + str(investment) + "!!!")
 
 choice = input("Try loopy program again? (y/n): ")
 if choice.lower() != "y":
     should_Exit = True
# end while loop
print("Bye!")


