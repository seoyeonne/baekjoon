import sys

n ,d = map(int,sys.stdin.readline().split())


cnt = 0
for i in range(1,n+1):
    irr = list(map(int,str(i)))
    cnt = cnt + irr.count(d)

print(cnt)

