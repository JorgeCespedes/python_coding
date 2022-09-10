
def insertionSort(list):
    '''Insertion sort using Python.'''
    for i in range(1, len(list)):
        currentNumber = list[i]
        for j in range(i - 1, -1, -1):
            if list[j] < currentNumber:
                list[j], list[j + 1] = list[j + 1], list[j]
            else:
                list[j + 1] = currentNumber
                break
    return list


if __name__ == '__main__':
    list = [3, 7, 2, 8, 4, 1, 9, 5]
    print('Sorted list: ', insertionSort(list))

