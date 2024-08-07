from math import sqrt
number = int(input())
numbers = []
for _ in range(number):
    numbers.append(int(input()))
for num in numbers:
    a = sqrt(num)
    a = str(a)
    a,b = a.split('.')
    if b == '0':
        print(a + '.' + '0000')
    else:
        print(a +'.' + b[:4])