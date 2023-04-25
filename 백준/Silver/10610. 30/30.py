import sys

n = list(map(int,sys.stdin.readline().strip()))

if 0 not in n :
    print(-1)
elif sum(n) % 3 != 0 :
    print(-1)
else :
    n.sort(reverse=True)
    print("".join(map(str,n)))