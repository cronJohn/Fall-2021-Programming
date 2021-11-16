import random

min = 1
max = 10

ranNum = str(random.randint(min,max))

numInput = input('Enter a number between ' + str(min) + ' and ' + str(max) + ': ')

if numInput == ranNum:
    print('You got it!')
else:
    print('Nope! The number was ' + ranNum)