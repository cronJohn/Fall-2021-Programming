#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_08 Fall 2021
# File:       Homework_08.py
# Purpose:    Phonebook
#######################################################

# create main function
def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # initialize name, phone number, and email arrays with size of array_size
    array_size = 10
    names_array = [''] * array_size
    phone_number_array = [''] * array_size
    email_array = [''] * array_size

    # loop array_size times to get user input
    for i in range(array_size):

        # call functions to get name, pn, and email
        # store them in respective arrays
        # +1 b\c it needs to start at 1 not 0
        names_array[i] = get_input_name(i + 1)
        phone_number_array[i] = get_input_phone_number(i + 1)
        email_array[i] = get_input_email(i + 1)

        # white space
        print()

    # white space
    print()

    # ask user for initial search value
    search_value = input('Enter search value: ')

    # keep asking user for input values unless they enter nothing
    while search_value != '':

        # show the table header at top
        display_table_header()

        # loop through all values so mulitple matches are printed
        for i in range(0, array_size):

            # if value in names_array has search value in it (case sensitive)
            if names_array[i].find(search_value) != -1:

                # output info to the user that has search_value in it
                print(names_array[i] + '\t\t' +
                      phone_number_array[i] + '\t' +
                      email_array[i])

        # white space
        print()

        # ask for more input
        search_value = input('Enter search value: ')


# function to ask user to input name based on name_count and returns it
def get_input_name(name_count):

    # ask the user for a name and return it
    return input('Enter name #' + str(name_count) + ':           ')


# function to ask user to input phone number based on pn_count and returns it
def get_input_phone_number(pn_count):

    # ask the user for a phone number and return it
    return input('Enter phone number #' + str(pn_count) + ':   ')


# function to ask user to input email based on email_count and returns it
def get_input_email(email_count):

    # ask the user for email and return it
    return input('Enter email address #' + str(email_count) + ':  ')


# function to display name, phone number, and email table flair
def display_table_header():
    print('Name\t\t\tPhone\t\tEmail')
    print('----\t\t\t-----\t\t-----')


# call main method
main()
