#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Practice_06 Fall 2021
# File:       Practice_06.py
# Purpose:    Kinetic energy formula
#######################################################

# create main method
def main():

    # add header to the top
    print('\n**  John Niemiec  **\n')

    # get user input for the object's mass and velocity
    entered_mass = float(input('Enter the mass of the object in kilograms: '))
    entered_velocity = float(input('Enter the velocity of the object in meters per second: '))

    # add whitespace
    print()

    # calculate the kinetic energy
    kinetic_energy = calculate_kinetic_energy(entered_mass, entered_velocity)

    # output the kinetic energy to the user
    print('Joules: ' + str(kinetic_energy))


# create function to calculate kinetic energy with mass and velocity
def calculate_kinetic_energy(mass, velocity):

    # return kinetic energy
    return (1/2) * mass * (velocity ** 2)


# call the main method
main()
