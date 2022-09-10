
def print_factors(x):
    '''Python Program to find the factors of a number'''
    print('The factor of', x, 'are: ')
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = int(input('Enter a number to find the factors: '))
print_factors(num)

