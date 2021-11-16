#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Project_01 Fall 2021
# File:       Project_01.py
# Purpose:    Factorial
#######################################################


# define the main method
def main():

    # header of the program
    print('\n**  John Niemiec  **\n')

    # this will be n! calculated and starts at 1 b/c it's bad to multiply by 0
    total = 1

    # get a number from the user to compute the factorial
    input_num = int(input('Enter a number greater than 1: '))

    # add whitespace
    print()

    # start the output to the user with the n! part
    print(str(input_num) + '! = ', end='')

    # loop through all values between 1 and n
    for i in range(1, input_num + 1):

        # multiply to the running total
        total *= i

        # if i < input_num or not the last value
        if i != input_num:

            # print normally with an x
            print(i, 'x ', end='')

        # if i == input_num or the last value
        else:

            # print without an x
            print(i, end='')

    # add the total to the output
    print(' =', total)


main()
