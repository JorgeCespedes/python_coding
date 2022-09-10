
def anagram(word1, word2):
    '''Validate Anagrams using Python'''
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


print(anagram('cool', 'loco'))
print(anagram('hola', 'leoe'))
