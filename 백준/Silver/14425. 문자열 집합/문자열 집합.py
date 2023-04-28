import sys

input = sys.stdin.readline
n,m = map(int,input().split())

cnt = 0

check = list(input() for i in range(n))
word= list(input() for i in range(m))

for i in word:
    if i in check:
        cnt = cnt + 1
print(cnt)