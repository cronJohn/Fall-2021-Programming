#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_05b Fall 2021
# File:       Practice_05b.py
# Purpose:    Turtle Spiral
#######################################################

# import the necessary turtle module for graphics stuff
import turtle


# create the main method
def main():

    # parameters to change number of squares, the square size, and rotation amount
    num_squares = 37
    start_size = 50
    size_increase_factor = 5
    ROTATION_AMOUNT = 10

    # header
    print('\n**  John Niemiec  **\n')

    # create a turtle object to be able to draw
    my_turtle = turtle.Turtle()

    # create a function to easily draw a square with side_length size
    def draw_square(side_length):
        for i in range(4):
            my_turtle.forward(side_length)
            my_turtle.right(90)

    # loop to draw num_squares amount of squares
    for i in range(1, num_squares + 1):

        # if drawing the first square
        if i == 1:

            # draw normally
            draw_square(start_size)

        # if not the first square
        else:

            # draw a square whose size increases by size_increase_factor every loop
            draw_square(start_size + i * size_increase_factor)

        # turn the turtle right by rotation amount
        my_turtle.right(ROTATION_AMOUNT)

    # don't close the program prematurely
    input('Press any key to exit: ')


# call the main method
main()
