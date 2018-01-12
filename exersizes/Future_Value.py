#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 11 January 2018

import sys

# display a welcome message
print("*************** PYTHON **************")
print("**  Erin\'s Future Value program  **")
print("*************** PYTHON **************")

should_Exit = False
yearly_interest_rate = monthly_investment = 0.0
years = 0
while not should_Exit:
 print()
# get input from the user
 try:
    monthly_investment = float(input("Enter monthly investment:\t"))
 except ValueError:
    print ("ERROR, monthly rate should be a number. Please try again.")
    continue
 try:
     yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
 except ValueError:
    print ("ERROR, yearly interest rate should be a number. Please try again.")
    continue
 try:
    years = int(input("Enter number of years:\t\t"))
 except ValueError:
    print ("ERROR, number of years should be an integer. Please try again.")
    continue

# convert yearly values to monthly values
 monthly_interest_rate = yearly_interest_rate / 12 / 100
 months = years * 12

# calculate future value
 total_investment = 0
 future_value = 0
 for i in range(months):
     future_value += monthly_investment
     monthly_interest_amount = future_value * monthly_interest_rate
     future_value += monthly_interest_amount
     total_investment += monthly_investment

# display the amount
 print("Your total investment would be:\t" + str(total_investment))
 print("Future value:\t\t\t" + str(round(future_value,2)))
 print()

 choice = input("Try Future Value program again? (y/n): ")
 if choice.lower() != "y":
     should_Exit = True
# end while loop
print("Bye!")


