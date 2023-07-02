import sys

n = int(sys.stdin.readline())
sum =0

arr = []

arr.append(0)
arr.append(1)
arr.append(1)

for i in range(3,n+1):
    arr.append(arr[i-2] + arr[i-1] )

print(arr[n])
