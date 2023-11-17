while True:
    def palindrome():
        word = input('What is the word?')
        if word == word[::-1]:
            print('Yes it is')
        else:
            print('No it is not a palindrome')
    palindrome()