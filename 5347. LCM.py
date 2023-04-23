import sys

n = int(sys.stdin.readline())


def GCD(a,b):
    if b == 0:
        return a
    else :
        return GCD(b,a%b)
for i in range(n):
    a,b = map(int,sys.stdin.readline().rsplit())
    result = a*b // GCD(a,b)
    print(result)