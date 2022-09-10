
'''Python program to find the factorial of a number'''

# to take input from the user
num = int(input('Enter a number: '))

factorial = 1

# check if the number is negative, positive or zero

if num < 0:
    print('Sorry, but factorial does not exits for negative numbers')
elif num == 0:
    print('The factorial zero is 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    else:
        print('The factorial', num, 'is', factorial)
