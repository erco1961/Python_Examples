#!/usr/bin/env python3

# an example Python program working with dictionaries
# by Erin Coffey
# 29 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import local module for welcome message
import stringer
# import module for tracking lost time
import timer

# import 3 different Object classes
from objects import Product, Book, Movie

AUTHOR = "Erin Coffey"
NAME = "Demonstrate polymorphism and Override"

def show_products(products):
    for product in products:
        print("PRODUCT DATA")
        print("Type:\t"+ str(type(product)))
        print("Name:\t", product.name)
        if isinstance(product, Book):
              print("Author:\t", product.author)
        if isinstance(product, Movie):
              print("Year:\t", product.year)
        print("Discount price:  {:.2f}".format(product.getDiscountPrice()))
        print()
    

# end show_products()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)

    # create tuple of Product objects
    products = (Book("Moby Dick", 19.99, 0, "Herman Melville"),
                Product("Heavy hammer", 9.95, 13),
                Movie("Blade Runner", 29.99, 0, 1984))
    print()
    print("This program creates 3 objects of different types and, uses polymorphism to display data on each object.")
    print()
    show_products(products)
   
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
