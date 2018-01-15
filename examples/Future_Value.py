#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 11 January 2018
import stringer
AUTHOR = "Erin"
NAME = "Future Value"

def calculate_future_value(monthly_investment, yearly_interest_rate, years=20):

  # convert yearly values to monthly values
  monthly_interest_rate = yearly_interest_rate / 12 / 100
  months = years * 12

  # calculate future value
  total_investment = future_value = 0

  for i in range(months):
     future_value += monthly_investment
     monthly_interest_amount = future_value * monthly_interest_rate
     future_value += monthly_interest_amount
     total_investment += monthly_investment

  return future_value, total_investment
# end calculate_future_value



def display_investment_results(years, totalInv, resulting_value):
  print("After " + str(years) + " years:\t\t")
  print("Total investment:\t\t" + str(totalInv))
  print("Future value:\t\t\t" + str(round(resulting_value,2)))
  print()
# end display_investment_results

def main():
  stringer.show_welcome(NAME)
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

    future_value, total_investment = calculate_future_value(monthly_investment, yearly_interest_rate, years)
    display_investment_results(years, total_investment, future_value)

    choice = input("See results for 20 year investment? (y/n): ")
    if choice.lower() == "y":
       # call using default value for years
       future_value, total_investment = calculate_future_value(monthly_investment, yearly_interest_rate)
       # call function using named args in alternative order
       display_investment_results(totalInv=total_investment, resulting_value=future_value, years=20)

    choice = input("Try Future Value program again? (y/n): ")
    if choice.lower() != "y":
      should_Exit = True

  # end while loop
# end main()
print("Bye!")

#if the current module is the main module
if __name__ == "__main__":
  main()
