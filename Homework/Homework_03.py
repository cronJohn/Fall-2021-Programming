#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_03 Fall 2021
# File:       Homework_03.py
# Purpose:    BMI calculation
#######################################################


# define main function
def main():

    # add header to the top
    print('\n**  John Niemiec  **\n')

    # ask the user for weight in pounds, and height in feet and inches
    user_weight = float(input('Pounds: '))
    user_height_feet = int(input('Feet: '))
    user_height_inches = float(input('Inches: '))

    # get the total amount of inches
    user_total_inches = user_height_feet * 12 + user_height_inches

    # add white space
    print()
    print()

    # output the user's bmi
    display_bmi(user_total_inches, user_weight)


# create function to calculate and display bmi based on weight and height
def display_bmi(total_inches, weight):

    # use height and weight to calculate bmi
    bmi = ((weight/(total_inches)**2) * 703)

    # output bmi to the user
    print('Your BMI is', bmi)


# call the main method
main()
