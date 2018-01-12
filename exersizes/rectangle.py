#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

# display a welcome message
print("***************** PYTHON *****************")
print("**  Erin\'s Area and Perimiter program   **")
print("***************** PYTHON *****************")
print()

# get input from the user
#miles_driven = float(input("Enter miles driven:\t\t"))
length = float(input("Enter length:\t"))
width = float(input("Enter width:\t"))

# calculate miles per gallon
area = round(length * width,2)
perimiter = round(length * 2 + width * 2,2)

# calculate total cost of gas
#total_cost = round(gallons_used * cost_per_gallon,2)

# calculate cost per mile
#cost_per_mile = round(total_cost / miles_driven,2)
            
# format and display the result
print()
#print("Miles Per Gallon:\t\t" + str(mpg))
#print("Total gas cost:\t\t\t" + str(total_cost))
#print("Cost per mile:\t\t\t" + str(cost_per_mile))
print("Area =\t\t",area)
print("Perimiter =\t",perimiter)
print()
print("Bye")


