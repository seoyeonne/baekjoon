import sys

n,m = map(int,sys.stdin.readline().split())


arr = [0 for i in range(n)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    for j in range(a-1,b):
        arr[j] = c

for i in arr:
    print(i,end=' ')