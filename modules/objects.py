"""
A module to use for defining various objects
"""

# an example python module for class definitions
# by Erin Coffey
# 30 January 2018

class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.name = name
        self.price = price # pass the price parameter to the setter and check validity there
        self.discountPercent = discountPercent
    # end __init__

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price must be greater than or equal to 0")
        else:
            self.__price = price

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100
    # end getDiscountAmount()

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
    # end getDiscountPrice()

# end class Product:

from dice import Die #should be in same directory as all other local modules!

class Game:
    def __init__(self):
        self.turn = 1
        self.score = 0
        self.scoreThisTurn = 0
        self.isTurnOver = False
        self.isGameOver = False
        self.die = Die()
    # end __init__
# end class Game:
