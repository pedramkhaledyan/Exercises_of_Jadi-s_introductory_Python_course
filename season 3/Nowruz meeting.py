a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

# we get the sum of the distance between each point and two other points
xa=abs(a-b)+abs(a-c)
xb=abs(b-a)+abs(b-c)
xc=abs(c-a)+abs(c-b)

if xa<xb and xa<xc:
    print(int(xa))
elif xb<xa and xb<xc:
    print(int(xb))
elif xc<xa and xc<xb:
    print(int(xc))