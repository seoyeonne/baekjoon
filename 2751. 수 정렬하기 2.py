import sys

arr = []
n = int(sys.stdin.readline())

for i in range(n):
    k = int(sys.stdin.readline())
    arr.append(k)

arr.sort()
for i in range(len(arr)):
    print(arr[i])