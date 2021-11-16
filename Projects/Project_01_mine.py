print('\n**  John Niemiec  **\n')

total = 1


def factorial(num):
    if num == 1:
        return 1

    else:
        return num * factorial(num - 1)


def print_stuff(input_num, total):
    print()
    print(f'{input_num}! = ', end='')
    print(f'{total}')


input_num = int(input('Enter a number: '))

total *= factorial(input_num)

print_stuff(input_num, total)
