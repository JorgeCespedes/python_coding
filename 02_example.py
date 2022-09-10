
def palindrome(sentence):
    '''Palindrome Words using Python'''
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i,'')
    palindrome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome


sentence = input('Enter your sentence: ')
print(palindrome(sentence))
    
