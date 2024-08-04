# 2 way for solve this program
 # first--------------------------------------------------

ballot = int(input())
country_list = list()
for i in range(ballot):
    country_list.append(input())

country_list.sort()
countries_votes = {name : country_list.count(name) for name in country_list}

for key,value in countries_votes.items():
    print(key,value)

 # second--------------------------------------------------

import collections

country_dict = {}
votes_number = int(input())
# use '_' in loop when we don't need loop variable in loop.
for _ in range(0,votes_number):
    country = input()
    country_dict[country] = country_dict.get(country,0)+1
    # If the country is already present in the dictionary, increment its count by 1.
    # If the country is not present, initialize its count to 0 and then add 1.

country_dict = collections.OrderedDict(country_dict)
country_li = list(country_dict)
country_li.sort()

for country in country_li:
    print(country,country_dict[country])