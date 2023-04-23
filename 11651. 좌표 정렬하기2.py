import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr_low = list(map(int,sys.stdin.readline().split()))
    arr.append(arr_low)

arr = sorted(arr,key = lambda x:(x[1],x[0]))

for x,y in arr:
    print(x,y)