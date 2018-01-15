"""
A module to use for converting between 
degrees Celsius and degrees Fahrenheit

*** NOTE ***
    ERROR (type) CHECKING SHOULD BE PERFORMED BY THE CALLER!!!
*** NOTE ***
"""

# an example python module
# by Erin Coffey
# 12 January 2018

def to_celsius(fahrenheit):
    """
    Accepts degrees Fahrenheit
    Returns degrees Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    """
    Accepts degrees Celsius
    Returns degrees Fahrenheit
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# use main for testing the functions in this module
def main():
    for temp in range(0, 212, 40):
        print(temp, "\tFahrenheit = ", round(to_celsius(temp)), "Celsius")
    print(212, "\tFahrenheit = ", round(to_celsius(212)), "Celsius")
    print()
    for temp in range(0, 120, 20):
        print(temp, "\tCelsius\t   = ", round(to_fahrenheit(temp)), "Fahrenheit")

# if this is the main module, run the tests in main()
if __name__ == "__main__":
    main()
