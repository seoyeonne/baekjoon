import sys

n,m = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,n+1)]

for i in range(m):
    tmp = 0
    a,b = map(int,sys.stdin.readline().split())
    tmp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = tmp

for i in arr:
    print(i,end=' ')