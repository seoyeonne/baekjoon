import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr_low = list(map(int,sys.stdin.readline().split()))
    arr.append(arr_low)

arr = sorted(arr,key=lambda x: (x[0],x[1]))

for i in range(n):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')
    print()



