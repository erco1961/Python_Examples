#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

# import local module for welcome message
import stringer

# import validation module for taking valid user input
import validation as val

#to fix rounding errors
from decimal import Decimal
from decimal import ROUND_HALF_UP

# currency formatting
import locale as lc

NAME = "Invoice"
AUTHOR = "Erin Coffey"

def main():
    stringer.show_welcome(NAME)
    should_Exit = False

    print()
    print("======================")
    print()
    print("The customer type can be:")
    print("\nRetail:'r'")
    print("or")
    print("Wholesale:'w'")
    print()
    print("======================")
    print()
         
    while not should_Exit:
        new_invoice_total = invoice_total = discount_percent = discount_amount = 0
        customer_type = "unknown_type" 

        
        # get customer_type from the user
        customer_type = input("Enter customer type (r/w):\t")
        order_total = Decimal(val.get_float("Enter order total:\t\t", 100000))
        order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)

        # determine discount for retail customer
        if customer_type.lower() == "r":
            customer_type = "Retail"
            if order_total > 0 and order_total < 100:
                discount_percent = Decimal("0")
            elif order_total >= 100 and order_total < 250:
                discount_percent = Decimal(".1")
            elif order_total >= 250 and order_total < 500:
                discount_percent = Decimal(".2")
            elif order_total >= 500:
                discount_percent = Decimal(".25")
                
        # determine discount for wholesale customer
        elif customer_type.lower() == "w":
            customer_type = "Wholesale"
            if order_total > 0 and order_total < 500:
                discount_percent = Decimal(".4")
            elif order_total >= 500:
                discount_percent = Decimal(".5")
                
        # customer is neither wholesale nor retail so discount_percent at zero
        else:
            customer_type = "Unknown"
    
        # calculate discount and new invoice total
        discount = order_total * discount_percent
        discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
            
        subtotal = order_total - discount
        tax_percent = Decimal(".05")
        sales_tax = subtotal * tax_percent
        sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)
        invoice_total = subtotal + sales_tax

        # display results
        # determine the region for the money
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        line = "{:20} {:>10}"
        print()
        print("Customer Type:          {:10}".format(customer_type))
        print(line.format("Order total:", lc.currency(order_total, grouping=True)))
        print(line.format("Discount:", lc.currency(discount, grouping=True)))
        print(line.format("Subtotal:", lc.currency(subtotal, grouping=True)))
        print(line.format("Sales tax:", lc.currency(sales_tax, grouping=True)))
        print(line.format("Invoice total:", lc.currency(invoice_total, grouping=True)))
        print()
        choice = input("Try again? (y/n): ")
        if choice.lower() != "y":
            should_Exit = True
        # end while loop
    print("Bye!")
# end main


#if the current module is the main module
if __name__ == "__main__":
  main()


