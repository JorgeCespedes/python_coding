
def count_character(s):
    '''Count Character Occurrences using Python'''
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

word = input('Enter your string: ')

count_character(word)
