#  I solved this exercise with two methods

Names=[]
for _ in range(3):
    Name=input().lower()
    Name.capitalize()
    # capitalize write first letter of name with big letter
    Names.append(Name)
for name in Names:
    print(name)
# ----------------------------
Names=[]
for _ in range(3):
    Name=input().lower()
    Name=Name[0].upper()+Name[1:]
    Names.append(name)
for name in Names:
    print(name)