import sys

def fac(n):
    if n ==0 or n ==1:
        return 1
    else :
        return fac(n-1) * n

a = int(sys.stdin.readline())
print(fac(a))