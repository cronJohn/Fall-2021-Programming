#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_04 Fall 2021
# File:       Homework_04.py
# Purpose:    Time converter
#######################################################

print('\n**  John Niemiec  **\n')

# initialize variable for the unit (min, hour, day)
unit = ''

# initialize variable for seconds to min/hour/day conversion
converted_time = 0


# ask the user for number of seconds
amount_of_seconds = int(input('Enter the number of seconds: '))


# add white space
print()


# if you have enough time to make a day or more
if amount_of_seconds >= 86400:
    # convert seconds to days
    converted_time = amount_of_seconds / 86400
    unit = ' days'

# if you have enough time to make an hour
elif amount_of_seconds >= 3600:
    # convert seconds to hours
    converted_time = amount_of_seconds / 3600
    unit = ' hours'

# if you have enough time to make a minute
elif amount_of_seconds >= 60:
    # convert seconds to minutes
    converted_time = amount_of_seconds / 60
    unit = ' minutes'


# seconds is less than 60
else:
    # leave the seconds as is
    pass


# output the converted time to the user
if amount_of_seconds >= 60:
    print(str(amount_of_seconds) + ' seconds is equal to ' + str(converted_time) + unit)

else:
    pass
