#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_03 Fall 2021
# File:       Practice_03.py
# Purpose:    Ticket calculator
#######################################################

# create constant global variables to represent the cost of each class of tickets
CLASS_A_COST = 15.25
CLASS_B_COST = 11.50
CLASS_C_COST = 9


def main():

    # add header to the top
    print('\n**  John Niemiec  **\n')

    # get user input for each amount of tickets
    num_a_tickets = int(input('Enter number of class A tickets: '))
    num_b_tickets = int(input('Enter number of class B tickets: '))
    num_c_tickets = int(input('Enter number of class C tickets: '))

    # add white space
    print()

    # call the calculate function to print the cost to the user
    calculate_total_ticket_cost(num_a_tickets, num_b_tickets, num_c_tickets)


# function that calculates the total cost of the tickets and prints the total
def calculate_total_ticket_cost(a_tickets, b_tickets, c_tickets):

    # calculate the total ticket cost
    total_ticket_cost = CLASS_A_COST * a_tickets + CLASS_B_COST * b_tickets + CLASS_C_COST * c_tickets

    # output the total cost of ticket to the user
    print('Total: $' + str(total_ticket_cost))


# call the main function
main()
