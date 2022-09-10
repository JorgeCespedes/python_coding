
def bubbleSort(list):
    '''Bubble sort using Python.'''
    for i in range(len(list)):
        for j in range(len(list) - 1,i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
    return list


if __name__ == '__main__':
    list = [7, 8, 1, 2, 9, 4, 6, 5]
    print('Sorted list: ',bubbleSort(list))


