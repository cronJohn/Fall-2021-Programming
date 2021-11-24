#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_12 Fall 2021
# File:       Practice_12.py
# Purpose:    Reverse a string
#######################################################

# create main function
def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # get string from user
    user_input_str = input("Please enter some text: ")

    # whitespace
    print()

    # create variables for output
    reverse_str = ''
    sum_of_digits = 0
    title_str = ''

    # create loop to go through indices from end of string to 0
    for number in range(len(user_input_str) - 1, -1, -1):

        # add each character to the beginning of the string
        reverse_str += user_input_str[number]

        # if charater is a digit
        if user_input_str[number].isdigit():

            # add to sum of digits
            sum_of_digits += int(user_input_str[number])

    # get array of each word in the string
    split_str_array = user_input_str.split()

    # create loop to go through each word in the string
    for word in split_str_array:

        # capitalize the first letter of each word -- aka title case
        title_str += word.title() + ' '

    # output stuff to the user
    print("Backwards:\t" + reverse_str)
    print("Sum of digits:\t" + str(sum_of_digits))
    print("Capitalized:\t" + title_str)


# call main
main()
