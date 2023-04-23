import sys
sys.setrecursionlimit(10**7)

def GCD(a,b):
    if b == 0:
        return a
    else :
        return GCD(b,a%b)

def Factor(a):
    if a == 0 or a==1:
        return a
    else :
        return a * Factor(a-1)

a,b = map(int,sys.stdin.readline().split())
a = Factor(a)
result = GCD(a,b)

print(result)
