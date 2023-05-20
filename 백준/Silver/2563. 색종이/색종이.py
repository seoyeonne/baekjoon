import sys

n = int(sys.stdin.readline())
arr = [[0 for j in range(100)] for i in range(100)]
cnt = 0

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            if arr[j][k] != 1 :
                arr[j][k] = 1
                cnt = cnt + 1

print(cnt)