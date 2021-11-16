#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice 4 Fall 2021
# File:       Practice_04.py
# Purpose:    Does your change equal exactly a dollar?
#######################################################

# print a header
print('\n**  John Niemiec  **\n')


# get user input
num_pennies = int(input('Enter number of pennies: '))
num_nickels = int(input('Enter number of nickels: '))
num_dimes = int(input('Enter number of dimes: '))
num_quarters = int(input('Enter number of quarters: '))


# create blank space
print()


# calculate the total amount of cash for coins
total_cash = num_pennies + (num_nickels * 5) + (num_dimes * 10) + (num_quarters * 25)


# output whether or not the user wins
if total_cash == 100:
    # show the user they won
    print('You win!')

# if the total cash doesn't equal a dollar
else:
    # show the user they lost
    print('Sorry, you have ' + str(total_cash) + ' cents.')
