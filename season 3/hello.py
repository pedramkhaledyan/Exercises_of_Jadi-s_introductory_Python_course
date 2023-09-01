word = input()

hello = 'hello'
i = 0
while i < len(word) or hello:
    """ The loop continues until i is smaller than the length of the word or the hello variable is not empty """
    if word[i] == hello[0]:
        hello = hello[1:]
        ''' We check the variable word letter by letter with the variable letters hello and if they are the same,
            the letter which is the first letter of the variable hello is deleted. and check another letter with this meyhod.
        '''
    i += 1

if not hello:
    print('Yes')
else:
    print('No')