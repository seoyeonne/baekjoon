import sys
arr = []
sum = 0

for i in range(5):
    n = int(sys.stdin.readline())
    arr.append(n)
    sum = sum + n
arr.sort()
print(int(sum/5))
print(arr[2])