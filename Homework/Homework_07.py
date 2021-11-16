#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_07 Fall 2021
# File:       Homework_07.py
# Purpose:    Calculate speeding violations
#######################################################

# create main method
def main():

    # add header to top of program
    print('\n**  John Niemiec  **\n')

    # get the initial speed limit
    entered_speed_limit = int(input('Please enter the speed limit: '))

    # add white space
    print()

    # keep asking for input if speed limit isn't between 20-70
    while entered_speed_limit <= 20 or entered_speed_limit >= 70:

        # output an error to the user to enter a valid number
        print('ERROR: Speed limit must be between 20 and 70')

        # add white space
        print()

        # ask the user to enter another number
        entered_speed_limit = int(input('Please enter the speed limit: '))

        # add white space
        print()

    # white space
    print()

    # get the initial speed
    entered_speed = int(input('Please enter vehicule speed: '))

    # keep asking for input if speed is not between speed limit and 199
    while entered_speed <= entered_speed_limit or entered_speed >= 200:

        # add white space
        print()

        # output error to user
        print('ERROR: Vehicle speed must be between ' +
              str(entered_speed_limit + 1) + ' and 199')

        # add white space
        print()

        # ask user to enter a new speed
        entered_speed = int(input('Please enter vehicule speed: '))

    # add white space
    print()

    # store the fine based on how much over the user is from the speed limit
    fine_total = calculate_fine(entered_speed, entered_speed_limit)

    # output fine to the user
    print('Exceeded speed limit by ' + calculate_speed_over(fine_total) +
          ' $' + str(calculate_fine(entered_speed, entered_speed_limit)) +
          ' fine.')


# Calculate speed over based on fine
def calculate_speed_over(fine):

    # Do I really have to comment this?
    if fine == 50:
        # speed is 1-10 mph over
        return '1-10 MPH.'

    elif fine == 75:
        # speed is 11-15 mph over
        return '11-15 MPH.'

    elif fine == 150:
        # speed is 16-20 mph over
        return '16-20 MPH.'

    else:
        # speed is 21+ mph over
        return '21+ MPH.'


def calculate_fine(speed, limit):

    # calculate how much over the limit the speed is
    exceeded_amount = speed - limit

    # Exceeded speed limit by 1-10 MPH
    if 1 <= exceeded_amount <= 10:
        # return fine of $50
        return 50

    # Exceeded speed limit by 11-15 MPH
    elif 11 <= exceeded_amount <= 15:
        # return fine of $75
        return 75

    # Exceeded speed limit by 16-20 MPH
    elif 16 <= exceeded_amount <= 20:
        # return fine of $150
        return 150

    # Exceeded speed limit by 21+ MPH
    else:
        # return fine of $300
        return 300


# call main method
main()
