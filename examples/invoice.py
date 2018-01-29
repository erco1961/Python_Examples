#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import local module for welcome message
import stringer
# import validation module for taking valid user input
import validation as val
# import module for tracking lost time
import timer

#to fix rounding errors
from decimal import Decimal
from decimal import ROUND_HALF_UP

# currency formatting
import locale as lc

# date, time, time-delta
from datetime import datetime, timedelta

NAME = "Invoice"
AUTHOR = "Erin Coffey"

def display_customer_types():
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
# end display_customer_types()

def get_invoice_date():
    while True:
        try:
            invoice_date_str = input("Enter the invoice date MM/DD/YYYY: ")
            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")
            break
        except Exception as e:
            print(invoice_date_str + " is not a valid format. Please try again.")
            continue
    return invoice_date

# end get_invoice_date()

def calculate_due_date(invoice_date):
    due_date = invoice_date + timedelta(days=30)
    current_date = datetime.now()
    days_late = (current_date - due_date).days

    return current_date, due_date, days_late

# end calculate_due_date()

def show_due_date(invoice_date, current_date, due_date, days_overdue):
        print()
        print("{:15} {:10} {:2} {:5}".format("Invoice date: ",
                                             invoice_date.strftime("%B"),
                                             invoice_date.strftime("%d"),
                                             invoice_date.strftime("%Y")))
        #print("Invoice date: " + invoice_date.strftime("%B %d %Y"))
        print("{:15} {:10} {:2} {:5}".format("Due date: ",
                                             due_date.strftime("%B"),
                                             due_date.strftime("%d"),
                                             due_date.strftime("%Y")))
        #print("Due date: " + due_date.strftime("%B %d %Y"))
        print("{:15} {:10} {:2} {:5}".format("Current date: ",
                                             current_date.strftime("%B"),
                                             current_date.strftime("%d"),
                                             current_date.strftime("%Y")))
        #print("Current date: " + current_date.strftime("%B %d %Y"))
        print()

        if days_overdue == 1:
            print("This invoice is one day overdue.")
        elif days_overdue > 1:
            print("This invoice is", days_overdue, "days overdue.")
        else:
            days_due = days_overdue * -1
            if days_due == 0:
                print("This invoice is due today.")
            elif days_due == 1:
                print("This invoice is due in one day.")
            else:
                print("This invoice is due in", days_due, "days.")
 
# end show_due_date()

def main():
    myTimer = timer.begin_timer()
    stringer.show_welcome(NAME)
    should_Exit = False

    while not should_Exit:
        new_invoice_total = invoice_total = discount_percent = discount_amount = 0
        customer_type = "unknown_type" 

        
        # get customer_type from the user
        display_customer_types()
        customer_type = input("Enter customer type (r/w):\t")
        order_total = Decimal(val.get_float("Enter order total:\t\t", 100000))
        order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)

        # get invoice date
        invoice_date = get_invoice_date()
        current_date, due_date, days_overdue = calculate_due_date(invoice_date)

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
        
        show_due_date(invoice_date, current_date, due_date, days_overdue)
        
        print()
        choice = input("Try again? (y/n): ")
        if choice.lower() != "y":
            should_Exit = True
        # end while loop
    timer.stop_timer(myTimer)
    print("Bye!")
# end main


#if the current module is the main module
if __name__ == "__main__":
  main()


