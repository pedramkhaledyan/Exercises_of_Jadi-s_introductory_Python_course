num = int(input())

laptops = []
price_laptop = 0
qulity_laptop = 0
happy_irsa = 0

for i in range(num) :
    laptops.append(input().split())
    # Save price and qulity of each laptop in laptops list
for lap in laptops :
        # put price and qulity of each laptop in price_laptop and qulity_laptop variables
        price_laptop = int(lap[0])
        qulity_laptop = int(lap[1])
        # We compare the price and quality of each laptop with the price and quality variables, and if the condition is correct, a number is added to the happy_irsa variable.
        for laptop in laptops:
            if int(laptop[0]) >= price_laptop and int(laptop[1]) < qulity_laptop :
                happy_irsa += 1

if happy_irsa == 0 :
    print('poor irsa')
else:
    print('happy irsa')