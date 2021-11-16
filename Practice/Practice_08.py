#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_08 Fall 2021
# File:       Practice_08.py
# Purpose:    Lottery
#######################################################

# obtain randomness
import random


# main function
def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # Named Constants
    NUMBER_OF_MACHINES = 7  # Number of lotto machines
    NUMBER_OF_BALLS = 10    # Number of balls in each machine

    # create num array to store random values
    random_array = [0] * NUMBER_OF_MACHINES

    # loop through all of the machines
    for counter in range(NUMBER_OF_MACHINES):

        # assign random value from 0 - n_o_b to index in array
        random_array[counter] = random.randint(0, NUMBER_OF_BALLS - 1)

    # start initial output
    print('The winning lottery numbers are:', end=" ")

    # loop through the array of random nums and print all values
    for element in range(NUMBER_OF_MACHINES):

        print(random_array[element], end=' ')


# call main method
main()
