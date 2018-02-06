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

    def getDescription(self):
        return self.name
    # end getDiscountPrice()

    # override the __str__() method from class Object
    def __str__(self):
        returnString = self.name + " | " + str(self.price)
        if self.discountPercent > 0:
            returnString += " | " + str(self.discountPercent) + "% off"
        return returnString

    # end __str()

# end class Product:

# class Book extends class Product
class Book(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, author =""):
        Product.__init__(self, name, price, discountPercent) # call parent class constructor
        self.author = author
    # end __init__

    # override the getDescription() method
    def getDescription(self):
        return Product.getDescription(self) + " by " + self.author
    # end getDescription()

# end classBook(Product)

# class Movie extends class Product
class Movie(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, year =0):
        Product.__init__(self, name, price, discountPercent) # call parent class constructor
        self.year = year
    # end __init__

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 1900:
            raise ValueError("Movies were not made before 1900")
        else:
            self.__year = year

    # override the getDescription() method
    def getDescription(self):
        return Product.getDescription(self) + " (" + str(self.year) + ")"
    # end getDescription()

# end classBook(Product)

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

#an example of a custom exception
class DataAccessError(Exception):
    pass
