import sys

arr = []
n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)

arr.sort()
for i in range(len(arr)):
    print(arr[i])