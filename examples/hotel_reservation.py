#!/usr/bin/env python3

# an example Python program working with string credentials as user input
# by Erin Coffey
# 24 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import local module for welcome message
import stringer
# import module for tracking lost time
import timer

from datetime import datetime
import locale

AUTHOR = "Erin Coffey"
NAME = "Hotel Reservation with date checking"
RATE = 100

def get_arrival_date():
    print()
    while True:
        date_str = input("Enter arrival date (YYYY-MM-DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(date_str + " is not a valid date format. Please try again.")
            continue
        #verify the arrival is not scheduled in the past
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print("Arrival date must be today or later. Please try again.")
            continue
        else:
            return arrival_date

# end get_arrival_date()

def get_departure_date(arrival_date):
    while True:
        date_str = input("Enter departure date (YYYY-MM-DD): ")
        try:
            departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(date_str + " is not a valid date format. Please try again.")
            continue

        if departure_date <= arrival_date:
            print("Departure date must be after arrival date. Please try again.")
            continue
        else:
            return departure_date            

# end departure_date = get_departure_date()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)

    while True:

        arrival_date = get_arrival_date()
        departure_date = get_departure_date(arrival_date)
        print()

        # calculate nights and cost
        rate_message = ""
        rate = RATE
        if arrival_date.month == 8:#August is high season
            rate_message = "(High Season Rates Apply)"
            rate = RATE * 1.25
        total_nights = (departure_date - arrival_date).days
        total_cost = total_nights * rate

        #display formatted results
        date_format = "%B %d, %Y"
        result = locale.setlocale(locale.LC_ALL, "")
        if result == "C":
            locale.setlocale(locale.LC_ALL, "en_US")

        print("Arrival:           ", arrival_date.strftime(date_format))
        print("Departure:         ", departure_date.strftime(date_format))
        print("Nightly rate:      ", locale.currency(rate), rate_message)
        print("Nights total:      ", total_nights)
        print("Price total:       ", locale.currency(total_cost))
        print()

        choice = input("Try \'" + NAME + "\' program again? (y/n): ")
        if choice.lower() != "y":
          break
    # end while loop
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
