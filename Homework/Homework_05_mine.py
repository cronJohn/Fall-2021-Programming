#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_05_mine Fall 2021
# File:       Homework_05_mine.py
# Purpose:    Convert Celsius to Fahrenheit
#######################################################

print('\n**  John Niemiec  **\n')


def CtoF(celsius):
    return 1.8 * celsius + 32


def main():
    start_cel = -15
    end_cel = 40
    step = 2.5

    while start_cel <= end_cel:
        converted_cel = CtoF(start_cel)
        print(f'{start_cel} degrees Celsius is {converted_cel}'
              ' degrees Fahrenheit.')
        start_cel += step


main()
