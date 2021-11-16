#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_05 Fall 2021
# File:       Homework_05.py
# Purpose:    Convert Celsius ot Fahrenheit
#######################################################

def main():
    # print name at top
    print('\n**  John Niemiec  **\n')


    # set variables to loop from, to, and the increment
    from_celsius = -15
    to_celsius = 40
    increment = 2.5


    # create a while loop to loop from from_celsius to to_celsius
    while from_celsius <= to_celsius:
        # get the Celsius temperature converted to Fahrenheit
        converted_temp = 1.8 * from_celsius + 32

        # output the Celsius and converted Fahrenheit temp to the user
        print(str(from_celsius) + ' degrees Celsius is ' + str(converted_temp) + ' degrees Fahrenheit.')

        # move on to the next Celsius temp by increment amount
        from_celsius += increment


main()
