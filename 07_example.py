
def selectionSort(list):
    '''Selection sort in Python'''
    for i in range(len(list) - 1):
        minimun = i
        for j in range(i + 1, len(list)):
            if(list[j] < list[minimun]):
                minimun = j
        if(minimun != i):
            list[i], list[minimun] = list[minimun], list[i]
    return list

if __name__ == '__main__':
    list = [4, 6, 9, 8, 1, 7, 3]
    print(selectionSort(list))
