strings = input()
count_U = 0
count_L = 0
for char in strings:
    if char == char.upper(): 
        count_U += 1
    else:
        count_L += 1
if count_U > count_L :
    print(strings.upper())
else:
    print(strings.lower())