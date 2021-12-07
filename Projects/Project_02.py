#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Project_02 Fall 2021
# File:       Project_02.py
# Purpose:    String to American Telephone Number
#######################################################

# create main function
def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # Get string from user
    input_str = input('Please enter some text or press <Enter> to exit: ')

    # start and continue loop if input_str is not empty
    while input_str != '':

        # whitespace
        print()
        print()

        # get the amount of lowercase and uppercase chars in input_str
        lower_case_count = count_lowercase_characters(input_str)
        upper_case_count = count_uppercase_characters(input_str)

        # output the lowercase and uppercase counts
        print('Lower case:\t\t' + str(lower_case_count))
        print('Upper case:\t\t' + str(upper_case_count))

        # output converted_telephone_str
        print('Telephone:\t\t' + convert_string_to_telephone_number(input_str))

        # create temp string that is input_str with words separated by spaces
        temp_str = input_str.split()

        # create first_letter_reversed_str variable
        first_letter_reversed_str = ''

        # loop through the string starting at the end and working backwards
        for i in range(len(temp_str) - 1, -1, -1):

            # get the first index of the word and add it to first_letter_reversed_str
            first_letter_reversed_str += temp_str[i][0]

        # output first_letter_reversed_str
        print('First letter reversed:  ' + first_letter_reversed_str)

        # whitespace
        print()

        # Get string from user
        input_str = input('Please enter some text or press <Enter> to exit: ')


# function to return the number of lowercase characters in a string
def count_lowercase_characters(input_str):

    # create lower_case_count
    lower_case_count = 0

    # loop through string
    for i in range(len(input_str)):

        # if character is lowercase
        if input_str[i].islower():
            # add 1 to lowercase count
            lower_case_count += 1

    # return lower_case_count
    return lower_case_count


# function to return the number of uppercase characters in a string
def count_uppercase_characters(input_str):

    # create upper_case_count
    upper_case_count = 0

    # loop through string
    for i in range(len(input_str)):

        # if character is uppercase
        if input_str[i].isupper():
            # add 1 to lowercase count
            upper_case_count += 1

    # return upper_case_count
    return upper_case_count


# function to convert string into telephone number
def convert_string_to_telephone_number(input_str):

    # create empty string
    converted_telephone_str = ''

    # loop through string
    for i in range(len(input_str)):

        # if character is a, b, or c
        if input_str[i].lower() == 'a' or input_str[i].lower() == 'b' or input_str[i].lower() == 'c':
            # add 2 to the string
            converted_telephone_str += '2'

        # if character is d, e, or f
        elif input_str[i].lower() == 'd' or input_str[i].lower() == 'e' or input_str[i].lower() == 'f':
            # add 3 to the string
            converted_telephone_str += '3'

        # if character is g, h, or i
        elif input_str[i].lower() == 'g' or input_str[i].lower() == 'h' or input_str[i].lower() == 'i':
            # add 4 to the string
            converted_telephone_str += '4'

        # if character is j, k, or l
        elif input_str[i].lower() == 'j' or input_str[i].lower() == 'k' or input_str[i].lower() == 'l':
            # add 5 to the string
            converted_telephone_str += '5'

        # if character is m, n, or o
        elif input_str[i].lower() == 'm' or input_str[i].lower() == 'n' or input_str[i].lower() == 'o':
            # add 6 to the string
            converted_telephone_str += '6'

        # if character is p, q, or r
        elif input_str[i].lower() == 'p' or input_str[i].lower() == 'q' or input_str[i].lower() == 'r' or input_str[i].lower() == 's':
            # add 7 to the string
            converted_telephone_str += '7'

        # if character is s, t, or u
        elif input_str[i].lower() == 't' or input_str[i].lower() == 'u' or input_str[i].lower() == 'v':
            # add 8 to the string
            converted_telephone_str += '8'

        # if character is v, w, or x
        elif input_str[i].lower() == 'w' or input_str[i].lower() == 'x' or input_str[i].lower() == 'y' or input_str[i].lower() == 'z':
            # add 9 to the string
            converted_telephone_str += '9'

        # if character is not a-z
        else:
            converted_telephone_str += input_str[i]

    # return converted_telephone_str
    return converted_telephone_str


# call main function
main()
