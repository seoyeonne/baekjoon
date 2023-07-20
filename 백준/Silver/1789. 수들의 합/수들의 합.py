import sys

s = int(sys.stdin.readline())
n = 0
sum = 0

while s >= sum:
    n = n + 1
    sum = sum + n
    if s < sum :
        break

print(n-1)