''' in first exercise we should find person who is older than everyone
'''

older_age=0
persons_age=int(input())

while persons_age != -1:

    if persons_age>older_age:
        older_age=persons_age
        persons_age=int(input())
    else:
      older_age=older_age
      persons_age=int(input())

print(older_age)

# =====================================================================

''' in second exercise we should find person who is older than everyone and second person who is older than everyone
'''

older_age_1=0
older_age_2=0
person_age=int(input())

while person_age != -1:
    # If a person is older than older_age_1 first we should put older_age_1 in older_age_2 then put new age in older_age_1
    if person_age > older_age_1:
        older_age_2=older_age_1
        older_age_1=person_age
    elif person_age > older_age_2:
        older_age_2=person_age
    person_age=int(input())

print(older_age_1,older_age_2)
