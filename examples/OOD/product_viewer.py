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
# import object classes
from objects import Product, Book, Movie
# ifor input validation 
import validation as val

AUTHOR = "Erin Coffey"
NAME = "Object Oriented Product Viewer"

def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i+1) + ". ",product,end="")# use overridden object string representation method
        if isinstance(product, Book):
            print(" (Book)")
        elif isinstance(product, Movie):
            print(" (Movie)")
        else:
            print()
    print()
# end show_products()

def show_product(product):
    print("PRODUCT DATA")
    print("Name:                              {:s}".format(product.name))
    if isinstance(product, Book):
        print("Author:                            {:s}".format(product.author))
    if isinstance(product, Movie):
        print("Year:                              {:d}".format(product.year))
    print("Price:                             {:.2f}".format(product.price))
    print("Discount percent:                  {:d}%".format(product.discountPercent))
    print("Discount amount:                   {:.2f}".format(product.getDiscountAmount()))
    print("Discount price:                    {:.2f}".format(product.getDiscountPrice()))
    print()
# end show_product()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    print()
    # tuple of product objects demonstrating polymorphism
    products = (Product("Heavy hammer", 12.99, 62),
                Product("Light nails", 5.06, 0),
                Movie("Blade Runner", 29.99, 0, 1984),
                Book("Moby Dick", 19.99, 0, "Herman Melville"),
                Product("Medium tape", 7.24, 0))
    show_products(products)

    while True:
        print()
        
        try:
            number = val.get_int("Enter Product number: ",len(products),0)
            product = products[number - 1]
            show_product(product)
                
        except Exception as e:
            print("There was an Error processing your product.", e)
            break

        choice = input("View another? (y/n): ").lower()
        if choice != "y":
            break

    # end while loop
        
    timer.stop_timer(myTimer)
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
