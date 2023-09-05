text=input()
if text==text[::-1]:
    # reverse a string by slicing the string and using a negative step of one
    print('palindrome')
else:
    print('not palindrome')