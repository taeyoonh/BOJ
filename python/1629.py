import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())

k=1

a=a%c
while b>0:
    if b%2==1:
        k*=a
    b//=2
    a=a**2%c

print(k%c)

#print(pow(a,b,c))