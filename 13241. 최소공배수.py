import sys

a,b = map(int,sys.stdin.readline().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

result = a * b // gcd(a,b)
print(result)
