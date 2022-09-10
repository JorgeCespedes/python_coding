from itertools import permutations

def allPermutations(str):
    '''Function to find permutations of a given string'''
    permList = permutations(str)
    # print all permutations
    for perm in list(permList):
        print(''.join(perm))
# Driver program

if __name__ == '__main__':
    str = input('Enter your string: ')
    allPermutations(str)
