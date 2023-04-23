import sys
a = []
b = []

n,m = map(int,sys.stdin.readline().split())

for i in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    a.append(arr)

m,k = map(int,sys.stdin.readline().split())
for j in range(m):
    brr = list(map(int,sys.stdin.readline().split()))
    b.append(brr)

for i in range(n):
    result = []
    for l in range(k):
        aa = 0
        for j in range(m):
            aa += a[i][j] * b[j][l]
        result.append(aa)
    print(*result)

