#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_05a Fall 2021
# File:       Practice_05a.py
# Purpose:    Sum of positive numbers
#######################################################

# print my name at the top
print('\n**  John Niemiec  **\n')


# configue main method
def main():

    # configure variables to store input and sum
    entered_num = 1
    total_sum = 0

    # keep asking for user input until they enter 0
    while entered_num != 0:
        # get user input
        entered_num = float(input('Enter a positive number'
                                  '(or zero when done): '))

        # add input to total
        total_sum += entered_num

    # whitespace
    print()

    # output the total sum to the user
    print('Sum: ' + str(total_sum))


# call main method
main()
