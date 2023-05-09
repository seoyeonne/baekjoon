import sys

n,m = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a-1:b] = reversed(arr[a-1:b])

for i in arr:
    print(i,end=' ')