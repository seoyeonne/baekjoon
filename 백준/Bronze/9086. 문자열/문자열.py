import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a = list(map(str,sys.stdin.readline().rstrip()))
    print(a[0],end="")
    print(a[len(a)-1])