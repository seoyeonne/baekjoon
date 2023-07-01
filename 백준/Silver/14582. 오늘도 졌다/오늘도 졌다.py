import sys

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

asum = 0
bsum = 0
k = 0

for i in range(len(a)):
    asum = asum + a[i]
    if asum > bsum:
        k = 1
    else :
        bsum = bsum + b[i]

if k == 1:
    print('Yes')
else :
    print('No')