import sys

arr = []
k = int(sys.stdin.readline())

for i in range(k):
    n = int(sys.stdin.readline())
    if (n != 0):
        arr.append(n)
    else :
        arr.pop()
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]

print(sum)