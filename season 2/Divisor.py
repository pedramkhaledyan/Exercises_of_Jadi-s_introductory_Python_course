def divisor(number):
    # this func calculates the divisor of the entered number and returns Number of divisors's entered number
    num_of_divisor=1
    for i in range(1,number):
        if number%i==0:
            num_of_divisor+=1
    return num_of_divisor

number_divisor=0
number_of_divisor=0
for i in range(1,21):
    number=int(input())
    if divisor(number) > number_of_divisor:
        number_of_divisor=divisor(number)
        number_divisor=number
    elif number_of_divisor==divisor(number):
        if number>number_divisor:
            number_divisor=number
            number_of_divisor=divisor(number)

print(number_divisor,number_of_divisor)