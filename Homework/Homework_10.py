#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_10 Fall 2021
# File:       Homework_10.py
# Purpose:    CSV file generator
#######################################################

# create main function
def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # create variable to continue/stop loop
    stop_program = False

    # clear output.csv file
    open('output.csv', 'w').close()

    # add header information to output.csv
    with open('output.csv', 'a') as csv_file:
        csv_file.write('Abbreviation,State,Population,Capital\n')

    # create loop to ask user for input
    while not stop_program:

        # get user input for state information
        user_input_state_initials = input("Please enter abbreviation of the state: ")
        user_input_state_name = input("Please enter the name of the state: ")
        user_input_state_population = input("Please enter the population of the state: ")
        user_input_state_capital = input("Please enter name of state's capital: ")

        # whitespace
        print()

        # overwrite and store information in CSV file called 'output.csv'
        with open('output.csv', 'a') as csv_file:
            csv_file.write(user_input_state_initials + ','
                           + user_input_state_name
                           + ',' + user_input_state_population
                           + ',' + user_input_state_capital + '\n')  # \n is new line

        # ask user if they want to continue
        stop_program = input("Would you like to continue? (y/n): ")

        # if user input is 'n'
        if stop_program == 'n':

            # end loop
            stop_program = True

        # if user input is 'y'
        else:

            # continue loop
            stop_program = False

        # whitespace
        print()


# call main
main()
