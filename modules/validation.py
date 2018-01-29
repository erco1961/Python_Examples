"""
A module to use for validating user input 
is a float or integer within specified limits
"""

# an example python module
# by Erin Coffey
# 15 January 2018

def get_float(message, high, low=0):
    """
    Takes a message from the caller and displays it in the console
    Takes a max and optional min value
    Accepts user input from console
    Returns a valid float value
    """

    while True:
        try:
            floatValue = float(input(message))
        except ValueError:
            print ("ERROR, Entry must be a number. Please try again.")
            continue
        if floatValue <= low or floatValue > high:
            print ("ERROR, Entry must be greater than " + str(low) + " and, less than or equal to "\
                + str(high) + ". Please try again.")
            continue
        break
    return floatValue
# end get_float

def get_int(message, high, low=0):
    """
    Takes a message from the caller and displays it in the console
    Takes a max and optional min value
    Accepts user input from console
    Returns a valid integer value
    """
    intValue = 1
    while True:
        try:
            intValue = int(input(message))
        except ValueError:
            print ("ERROR, Entry must be a number. Please try again.")
            continue
        if intValue <= low or intValue > high:
            print ("ERROR, Entry must be greater than " + str(low) + " and, less than or equal to "\
                + str(high) + ". Please try again.")
            continue
        break
    return intValue
# end get_int()

# use main for testing the functions in this module
def main():
    print ("\nTesting get_float('enter float:', 100, 0)\n\n")
    myFloat = get_float("enter float:\t", 100, 0)
    print("The float value returned is " + str(myFloat))

    print ("\nTesting get_int('enter int:', 100, 0)\n\n")
    myInt = get_int("enter integer:\t", 100, 0)
    print("The integer value returned is " + str(myInt))

# if this is the main module, run the tests in main()
if __name__ == "__main__":
    main()
