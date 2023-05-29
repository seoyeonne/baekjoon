import sys
from fractions import Fraction

def fac(m):
    if m ==0 or m ==1:
        return 1
    else :
        return int(fac(m-1) * m)

n,m = map(int,sys.stdin.readline().split())

print(Fraction(fac(n), (fac(m)*fac(n-m))))
