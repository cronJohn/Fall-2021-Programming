#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_09 Fall 2021
# File:       Homework_09.py
# Purpose:    Sort n' search
#######################################################

# create main function
def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # create array to store 20 names
    names_array = [''] * 20

    # allow the user to start entering names
    print('Please enter 20 names: ')

    # start looping 20 times with index going from 0 - 19
    for index in range(0, 20):

        # get the name from the user and store value at index
        names_array[index] = input(str((index + 1)) + ': ')

    # get new names_array that is sorted
    new_sorted_array = sort_array(names_array)

    # whitespace
    print()

    # output the sorted names to the user
    print('The sorted names are:')

    # for every name in the array
    for name in new_sorted_array:

        # print it out
        print(name)

    # whitespace
    print()

    # start init user input
    inputed_name = input('Enter a name to search for <or enter to exit>: ')
    print()

    # start a loop to search for names and exit if user hits enter
    while inputed_name != '':

        # use binary search to find the value

        # set initial values
        left = 0
        right = len(new_sorted_array) - 1
        position = -1
        array_lookups = 0
        found = False

        # start loop for value and continue if
        # value isn't found and it hasn't finished searching
        while not found and left <= right:

            # get middle value
            middle = (left + right) // 2

            # if the middle value is the search value
            if new_sorted_array[middle] == inputed_name:

                # set found to true
                found = True

                # increment array_lookups
                array_lookups += 1

                # set position to middle
                position = middle

                print('Name found: ' + new_sorted_array[position])
                print('Position: ' + str(position))
                print('Array lookups ' + str(array_lookups))
                print()

            # if the middle value is greater than the search value
            elif new_sorted_array[middle] > inputed_name:

                # set right to middle - 1
                right = middle - 1

                # increment array_lookupso
                array_lookups += 1

            # if the middle value is less than the search value
            elif new_sorted_array[middle] < inputed_name:

                # set left to middle + 1
                left = middle + 1

                # increment array_lookups
                array_lookups += 1

        # if no name is found
        if not found:
            # output no name found
            print('Name not found')
            print('Array lookups ' + str(array_lookups))
            print()

        # ask user for more input
        inputed_name = input('Enter a name to search for <or enter to exit>: ')
        print()


# create function to sort a given array of names and return sorted array
def sort_array(array):

    # use bubble sort by starting loop
    for index in range(0, len(array) - 1):

        # start the second loop
        for index2 in range(0, len(array) - 1):

            # if the current value is greater than the next value
            if array[index2] > array[index2 + 1]:

                # swap the values
                array[index2], array[index2 +
                                     1] = array[index2 + 1], array[index2]

    return array


# call the main function
main()
