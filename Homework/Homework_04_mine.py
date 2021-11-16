#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_04 Fall 2021
# File:       Homework_04.py
# Purpose:    Time converter
#######################################################

print('\n**  John Niemiec  **\n')

# functions to simplify time conversion


def get_days(seconds):
    """Returns how many days there are in x seconds"""

    max_time = 86400
    return seconds / max_time


def get_hours(seconds):
    """Returns how many hours there are in x seconds"""

    max_time = 3600
    return seconds / max_time


def get_minutes(seconds):
    """Returns how many minutes there are in x seconds"""

    max_time = 60
    return seconds / max_time


def choose_conversion(seconds):
    """Chooses the right conversion to perform based on x seconds

        Returns:
            list: [time_converted, units]
    """

    # compare seconds to find out the right conversion
    if seconds >= 86400:
        return [get_days(seconds), 'days']
    elif seconds >= 3600:
        return [get_hours(seconds), 'hours']

    elif seconds >= 60:
        return [get_minutes(seconds), 'minutes']
    else:
        return [seconds, 'seconds']


# main function to handle outputting results to the user
def main(seconds):
    time_amount, unit = choose_conversion(seconds)  # list unpacking
    print()
    print(f'{seconds} seconds is equal to {time_amount} {unit}.')


# input and output
main(int(input('Enter the number of seconds: ')))
