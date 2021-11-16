#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_02 Fall 2021
# File:       Practice_02.py
# Purpose:    Grocery store
#######################################################

print('\n**  John Niemiec  **\n')

# vars
counter = 1

sub_total = 0
total_amount = 0

tax_rate = 0.06
tax_amount = 0

# user input
while counter <= 5:
    item = float(input('Enter the price for item #' + str(counter) + '  '))
    sub_total += item
    tax_amount += item * tax_rate
    total_amount = sub_total + tax_amount
    counter += 1


# output
print()
print('Subtotal:   $' + str(sub_total))
print('Tax:        $' + str(tax_amount))
print('Total:      $' + str(total_amount))
