# Mini-project from Automate the Boring Stuff, Ch. 3

# iterative implementation of Collatz Conjecture
def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)

# recursive implementation of Collatz Conjecture
def collatz_recurs(number):
    if number == 1:
        return
    elif number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    collatz_recurs(number)

# validate user input
def user_input():
    while True:
        try:
            number = int(input('Enter a non-negative, non-zero integer: '))
            if number < 1:
                raise ValueError
            return number
        except ValueError:
            print('You must enter a non-negative, non-zero integer.')

if __name__ == '__main__':
    number = user_input()
    print()
    print('Iterative implementation:')
    collatz(number)
    print()
    print('Recursive implementation:')
    collatz_recurs(number)
