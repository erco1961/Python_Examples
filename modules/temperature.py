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

class Temp:
    def __init__(self):
        self.__celsius = 0.0
    # end __init__

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, celsius):
        self.__celsius = celsius
        print("From C setter, self.__celsius is ", self.__celsius)
        self.__fahrenheit = getFahrenheit(celsius)

    @property
    def fahrenheit(self):
        return self.__fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        self.__fahrenheit = fahrenheit
        print("From F setter, self.__fahrenheit is ", self.__fahrenheit )
        self.__celsius = getCelsius(fahrenheit)

    
    def getCelsius(self, fahrenheit):
        """
        Accepts degrees Fahrenheit
        Returns degrees Celsius
        """
        self.__fahrenheit = fahrenheit
        temp = (self.__fahrenheit - 32) * 5/9
        return round(temp, 2)

    def getFahrenheit(self, celsius):
        """
        Accepts degrees Celsius
        Returns degrees Fahrenheit
        """
        self.__celsius = celsius
        temp = self.__celsius * 9/5 + 32
        return round(temp, 2)
# end class Temp:

# use main for testing the functions in this module
def main():
    converter = Temp()
    for temp in range(0, 212, 40):
        print(temp, "\tFahrenheit = ", converter.getCelsius(temp), "Celsius")
    print(212, "\tFahrenheit = ", converter.getCelsius(212), "Celsius")
    print()
    for temp in range(0, 120, 20):
        print(temp, "\tCelsius\t   = ", converter.getFahrenheit(temp), "Fahrenheit")
 #   print(91, "\tCelsius\t   = ", converter.getFahrenheit(91), "Fahrenheit")

# if this is the main module, run the tests in main()
if __name__ == "__main__":
    main()
