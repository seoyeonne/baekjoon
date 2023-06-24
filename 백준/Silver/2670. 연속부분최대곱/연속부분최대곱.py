import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    a = float(sys.stdin.readline())
    arr.append(a)

for i in range(1,n):
    arr[i] = max(arr[i],arr[i]*arr[i-1])

print('%0.3f'%max(arr))