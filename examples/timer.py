"""
A module to use for calculating elapsed time

*** NOTE ***
    ERROR (type) CHECKING SHOULD BE PERFORMED BY THE CALLER!!!
*** NOTE ***
"""
# for test
import time as timid

from datetime import datetime, time

# by Erin Coffey
# 15 January 2018

def begin_timer():
    """
    Accepts nothing
    Returns a datetime object
    """

    start_time = datetime.now()
    return start_time

# end begin_timer()

def stop_timer(start_time):
    """
    Accepts datetime object
    Returns datetime object with elapsed time relative to current time
    """
    print("START_TIME:", start_time)

    stop_time = datetime.now()
    print("STOP_TIME: ", stop_time)

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60 #truncate result
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds
    hours = minutes // 60
    minutes = minutes % 60
    time_object = time(hours, minutes, seconds, microseconds)
    print("ELAPSED_TIME")
    if days > 0:
        print("Days:",days)

    print("Time:", elapsed_time)

 #   return days, time_object
# end stop_timer()

# use main for testing the functions in this module
def main():
    print("Running test...\n")
    start_time = begin_timer()
 #   print("START_TIME:", start_time)
    print("Take a nap for a second...\n")
    timid.sleep(1)
    stop_timer(start_time)
 #   days, elapsed_time = stop_timer(start_time)


    print("\nSuccess!")

# if this is the main module, run the tests in main()
if __name__ == "__main__":
    main()
