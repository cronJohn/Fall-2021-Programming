#######################################################
# Name:       John Niemiec
# Class:      CIS-1400
# Assignment: Homework_06 Fall 2021
# File:       Homework_06.py
# Purpose:    Grade calculator
#######################################################

def main():

    # add header to top
    print('\n**  John Niemiec  **\n')

    # get user input for each of the 5 test scores
    entered_grade_1 = float(input('Enter test score #1: '))
    entered_grade_2 = float(input('Enter test score #2: '))
    entered_grade_3 = float(input('Enter test score #3: '))
    entered_grade_4 = float(input('Enter test score #4: '))
    entered_grade_5 = float(input('Enter test score #5: '))

    # whitespace
    print()

    # round the average test score
    rounded_test_score = round(calc_average(entered_grade_1, entered_grade_2, entered_grade_3, entered_grade_4, entered_grade_5), 1)

    # output the results to the user
    print('Results:')
    print('Test #1: ' + determine_grade(entered_grade_1))
    print('Test #2: ' + determine_grade(entered_grade_2))
    print('Test #3: ' + determine_grade(entered_grade_3))
    print('Test #4: ' + determine_grade(entered_grade_4))
    print('Test #5: ' + determine_grade(entered_grade_5))
    print('-------- ----')
    print('Average: ' + str(rounded_test_score))


# create function that gets the average of 5 scores
def calc_average(score_1, score_2, score_3, score_4, score_5):

    # return the average of 5 scores
    return (score_1 + score_2 + score_3 + score_4 + score_5) / 5


# create function to return test score
def determine_grade(test_score):

    # if score is 90-100
    if test_score >= 90:

        # return letter grade A
        return 'A'

    # if score is 80-89
    elif test_score >= 80:

        # return letter grade B
        return 'B'

    # if score is 70-79
    elif test_score >= 70:

        # return letter grade C
        return 'C'

    # if score is 60-69
    elif test_score >= 60:

        # return letter grade D
        return 'D'

    # if score is < 60
    else:

        # return letter grade F
        return 'F'


# call the main method
main()
