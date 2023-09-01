string=input().lower()
for char in string:
    if char =='a' or char =='e' or char == 'i' or char == 'o' or char == 'u':
        string=string.replace(char,'')
string='.'.join(string)
# The join method adds dots between the characters of a string
print('.'+string)
