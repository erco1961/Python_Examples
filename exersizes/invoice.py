#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 10 January 2018

import sys

# display a welcome message
print("***************** PYTHON ******************")
print("*********  Erin\'s Invoice program  ********")
print("***************** PYTHON ******************")

customer_type = "unknown_type"  
new_invoice_total = invoice_total = discount_percent = discount_amount = 0
should_Exit = False
while not should_Exit:
 print()
 print("======================")
 print()
# get customer_type from the user
 try:
    customer_type = input("Enter customer type (r/w):\t")
    invoice_total = float(input("Enter invoice total:\t\t"))
 except ValueError:
    print ("ERROR, invoice total must be a number. Please try again.")
    continue

# determine discount for retail customer
 if customer_type.lower() == "r":
    if invoice_total > 0 and invoice_total < 100:
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total < 250:
        discount_percent = .1
    elif invoice_total >= 250 and invoice_total < 500:
        discount_percent = .2
    elif invoice_total >= 500:
        discount_percent = .25 
# determine discount for wholesale customer
 elif customer_type.lower() == "w":
    if invoice_total > 0 and invoice_total < 500:
        discount_percent = .4
    elif invoice_total >= 500:
        discount_percent = .5
# customer is neither wholesale nor retail so discount_percent at zero
 else:
    customer_type = "unknown_type"
    
# calculate discount and new invoice total
 if customer_type == "unknown_type":
    new_invoice_total = invoice_total
 else:
    discount_amount = round(invoice_total * discount_percent, 2)
    new_invoice_total = invoice_total - discount_amount

# display results
 print()
 print("Customer Type:\t\t\t" + customer_type)
 print("Invoice Total:\t\t\t" + str(invoice_total))
 print("Discount Percent:\t\t" + str(discount_percent))
 print("Discount Amount:\t\t" + str(discount_amount))
 print("New Invoice Total:\t\t" + str(new_invoice_total))
        
 choice = input("Try again? (y/n): ")
 if choice.lower() != "y":
     should_Exit = True
# end while loop
print("Bye!")


