#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_02 Fall 2021
# File:       Homework_02.py
# Purpose:    Acreage calculator
#######################################################

print('\n**  John Niemiec  **\n')

# user input
length = float(input('What is the length in feet? '))
width = float(input('What is the width in feet? '))

# calculate
acreage = length * width / 43560

# output
print()
print('The property is', acreage, 'acres')
