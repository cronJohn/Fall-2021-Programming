#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: ExtraCredit Fall 2021
# File:       ExtraCredit.py
# Purpose:    Geometry calculator
#######################################################

# import math module
import math


# create main function
def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # print menu
    print_menu()

    # ask user for input
    user_input = int(input('Enter your choice (1-4): '))

    # create while loop to keep asking for input
    while user_input != 4:

        # if user input is 1, call area_circle function
        if user_input == 1:
            calculate_area_circle()

        # if user input is 2, call area_rectangle function
        elif user_input == 2:
            calculate_area_rectangle()

        # if user input is 3, call area_triangle function
        elif user_input == 3:
            calculate_area_triangle()

        # if user input is not 1, 2, 3, or 4, print error
        else:
            print('ERROR: Enter a valid number between 1 and 4')

        if user_input >= 1 and user_input <= 4:
            # print menu
            print_menu()

            # ask user for input again
            user_input = int(input('Enter your choice (1-4): '))

        else:  # custom menu for error message
            user_input = int(input('Please enter your menu choice: '))


# create function to print menu
def print_menu():

    print('1. Calculate the Area of a Circle')
    print('2. Calculate the Area of a Rectangle')
    print('3. Calculate the Area of a Triangle')
    print('4. Quit')


# create function to calculate area of a circle
def calculate_area_circle():

    # print header
    print('\n---Area for a Circle---')

    # ask user for radius
    radius = float(input('Enter the radius: '))

    # loop for a good radius
    while radius <= 0:
        print('ERROR: Enter a valid number')
        radius = float(input('Please enter the radius: '))

    # calculate area of circle
    area = math.pi * radius * radius

    # print area
    print('The answer is:   ', area, '\n')


# create function to calculate area of a triangle
def calculate_area_triangle():

    # print header
    print('\n---Area for a Triangle---')

    # ask user for base
    base = float(input('Enter the base: '))

    # loop for a good base
    while base <= 0:
        print('ERROR: Enter a valid number')
        base = float(input('Please enter the base: '))

    # ask user for height
    height = float(input('Enter the height: '))

    # loop for good height
    while height <= 0:
        print('ERROR: Enter a valid number')
        height = float(input('Please enter the height: '))

    # calculate area of triangle
    area = (base * height) / 2

    # print area
    print('The answer is:   ', area, '\n')


# create function to calculate area of a rectangle
def calculate_area_rectangle():

    # print header
    print('\n---Area for a Rectangle---')

    # ask user for base
    base = float(input('Enter the base: '))

    # loop for a good base
    while base <= 0:
        print('ERROR: Enter a valid number')
        base = float(input('Please enter the base: '))

    # ask user for width
    width = float(input('Enter the width: '))

    # loop for good height
    while width <= 0:
        print('ERROR: Enter a valid number')
        width = float(input('Please enter the width: '))

    # calculate area of the rectangle
    area = base * width

    # print area
    print('The answer is:   ', area, '\n')


# call main function
main()
