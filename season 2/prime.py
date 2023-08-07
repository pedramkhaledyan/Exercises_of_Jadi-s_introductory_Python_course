# Determining whether a number is prime

number=int(input())
count=1
# count variable Counts the number of numbers that are divisible by the input number

for i in range(1,number):
    if number%i==0:
        count+=1

if count>2:
    print('not prime')
else:
    print('prime')