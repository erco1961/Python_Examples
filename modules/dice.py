"""
A module to use for defining die and dice objects
using object composition ans encapsulation
"""

# an example python module for class definitions
# by Erin Coffey
# 30 January 2018

import random

class Die:
    def __init__(self):
        self.__value = self.roll()#make private
    # end __init__

    @property               # read only
    def value(self):
        return self.__value
    # end @property value()

    def getValue(self):
        return self.__value
    # end getValue()

    def roll(self):
        self.__value = random.randrange(1,7)
 #       return self.__value
    # end roll()
        
    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        else:
            self.__value = value
    # end @value.setter Value()

    def getImage(self):
        if self.value == 1:
            self.__image = " _____ \n" + \
                  "|     |\n" + \
                  "|  o  |\n" + \
                  "|_____|"
        elif self.value == 2:
            self.__image = " _____ \n" + \
                  "|o    |\n" + \
                  "|     |\n" + \
                  "|____o|"
        elif self.value == 3:
            self.__image = " _____ \n" + \
                  "|o    |\n" + \
                  "|  o  |\n" + \
                  "|____o|"
        elif self.value == 4:
            self.__image = " _____ \n" + \
                  "|o   o|\n" + \
                  "|     |\n" + \
                  "|o___o|"
        elif self.value == 5:
            self.__image = " _____ \n" + \
                  "|o   o|\n" + \
                  "|  o  |\n" + \
                  "|o___o|"
        else:
            self.__image = " _____ \n" + \
                  "|o   o|\n" + \
                  "|o   o|\n" + \
                  "|o___o|"
        return self.__image

    @property
    def image(self):
        self.__image = self.getImage()# set the read-only attribute

        

##    def SetValue(self, value):
##        if value < 1 or value > 6:
##            raise ValueError("Die value must be from 1 to 6.")
##        else:
##            self.__value = value
    # end SetValue()



# end class Die

class Dice:
    def __init__(self):
        self.__list = []
    # end __init__

    @property                       # read only
    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple

    # end @property list()
    def addDie(self, die):
        self.__list.append(die)
    # end addDie()

    def rollAll(self):
        for die in self.__list:
            die.roll()

    # create iterator and next methods for this class
    def __iter__(self):
        self.__index = -1           # initialize index for each iteration
        return self

    def __next__(self):
        if self.__index >= len(self.__list) - 1:
            raise StopIteration()
        self.__index += 1
        die = self.__list[self.__index]
        return die
    
    # end rollAll()
# end class Dice 
