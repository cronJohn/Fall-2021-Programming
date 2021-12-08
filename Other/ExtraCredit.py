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
    user_input = int(input('Enter your choice (1-4). '))

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
            print('\nError! Please enter a valid choice.\n')

        # print menu
        print_menu()

        # ask user for input again
        user_input = int(input('Enter your choice (1-4). '))

    # end program
    print('Thanks for using the Geometry Calculator!')


# create function to print menu
def print_menu():

    print('\tGeometry Calculator')
    print('1. Calculate the Area of a Circle')
    print('2. Calculate the Area of a Rectangle')
    print('3. Calculate the Area of a Triangle')
    print('4. Quit\n')


# create function to calculate area of a circle
def calculate_area_circle():

    # ask user for radius
    radius = float(input('Enter the radius of the circle: '))

    # calculate area of circle
    area = math.pi * radius * radius

    # print area
    print('\nThe area of the circle is:', area, '\n')


# create function to calculate area of a triangle
def calculate_area_triangle():

    # ask user for base and height
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))

    # calculate area of triangle
    area = (base * height) / 2

    # print area
    print('\nThe area of the triangle is:', area, '\n')


# create function to calculate area of a rectangle
def calculate_area_rectangle():

    # ask user for width and height
    width = float(input('Enter the width of the rectangle: '))
    height = float(input('Enter the height of the rectangle: '))

    # calculate area of rectangle
    area = width * height

    # print area
    print('\nThe area of the rectangle is:', area, '\n')


# call main function
main()
