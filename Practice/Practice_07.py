#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_07 Fall 2021
# File:       Practice_07.py
# Purpose:    Payroll System
#######################################################

# create global constants for minimum and maximum hourly rates
MINIMUM_HOURLY_RATE = 7.50
MAXIMUM_HOURLY_RATE = 18.25
MAXIMUM_WEEKLY_HOURS = 40


# create the main method
def main():

    # add header to the top
    print('\n**  John Niemiec  **\n')

    # set up variables for entered hours and rate
    user_entered_hours = get_hours()
    user_entered_rate = get_rate()

    # calculate gross pay
    user_gross_pay = user_entered_hours * user_entered_rate

    # output gross pay to the user
    print('Gross Pay:  ' + str(user_gross_pay))


# create function to get hours worked
def get_hours():

    # get the initial number of hours
    num_hours_worked = float(input('Enter the number of hours worked: '))

    # add white space
    print()

    # loop until the user enters a valid number for hours worked between 0-MWH
    while num_hours_worked < 0 or num_hours_worked > MAXIMUM_WEEKLY_HOURS:

        # output error to the user
        print('ERROR - Invalid number of hours!')

        # add white space
        print()

        # ask the user to input another number
        num_hours_worked = float(input('Enter the number of hours worked: '))

        # add white space
        print()

    # add white space
    print()

    return num_hours_worked


def get_rate():

    # get initial rate from the user
    hourly_rate = float(input('Enter hourly rate: '))

    # loop until the user enters a valid rate between MinHR-MaxHR
    while hourly_rate < MINIMUM_HOURLY_RATE or hourly_rate > MAXIMUM_HOURLY_RATE:

        # add white space
        print()

        # output error to the user
        print('ERROR - Invalid number of hourly rate!')

        # add white space
        print()

        # ask user to input rate between 7.50-18.25
        hourly_rate = float(input('Enter hourly rate: '))

    # add white space
    print()

    return hourly_rate


# call main method
main()
