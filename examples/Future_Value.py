#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 11 January 2018

# import stringer module for welcome message
import stringer
# import validation module for taking valid user input
import validation

# for rounding errors
from decimal import Decimal

# currency formatting
import locale as lc

AUTHOR = "Erin Coffey"
NAME = "Future Value"

def calculate_future_value(monthly_investment, yearly_interest_rate, years=20):

  # convert yearly values to monthly values
  monthly_interest_rate = yearly_interest_rate / 12 / 100
  months = years * 12

  # calculate future value
  total_investment = future_value = Decimal("0.00")

  for i in range(months):
     future_value += monthly_investment
     monthly_interest_amount = future_value * monthly_interest_rate
     future_value += monthly_interest_amount
     future_value = future_value.quantize(Decimal("1.00"))
     total_investment += monthly_investment
     total_investment = total_investment.quantize(Decimal("1.00"))
     
  return future_value, total_investment
# end calculate_future_value

def display_investment_results(monthly_investment, years, totalInv, resulting_value):
  # determine the region for the money
  result = lc.setlocale(lc.LC_ALL, "")
  if result == "C":
    lc.setlocale(lc.LC_ALL, "en_US")
  line = "{:20} {:>10}"
  print("After " + str(years) + " years...\n")
  print(line.format("Monthly investment:", lc.currency(monthly_investment, grouping=True)))
  print(line.format("Total investment:", lc.currency(totalInv, grouping=True)))
  print(line.format("Future value:", lc.currency(resulting_value, grouping=True)))
  print()
# end display_investment_results

def main():
  stringer.show_welcome(NAME)
  should_Exit = False
  yearly_interest_rate = monthly_investment = Decimal("0.00")
  years = 0
  while not should_Exit:
    print()
    # get validated input from the user
    monthly_investment = Decimal(validation.get_float("Enter monthly investment:\t", 1000))
    yearly_interest_rate = Decimal(validation.get_float("Enter yearly interest rate:\t", 15))
    years = validation.get_int("Enter number of years:\t\t", 50)

    future_value, total_investment = calculate_future_value(monthly_investment, yearly_interest_rate, years)
    display_investment_results(monthly_investment, years, total_investment, future_value)

    if years != 20:
      choice = input("See results for 20 year investment? (y/n): ")
      if choice.lower() == "y":
        # call using default value for years
        future_value, total_investment = calculate_future_value(monthly_investment, yearly_interest_rate)
        # call function using named args in alternative order
        display_investment_results(monthly_investment, totalInv=total_investment, resulting_value=future_value, years=20)

    choice = input("Try Future Value program again? (y/n): ")
    if choice.lower() != "y":
      should_Exit = True

  # end while loop
# end main()
print("Bye!")

#if the current module is the main module
if __name__ == "__main__":
  main()
