import sys

n,m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
brr = list(map(int,sys.stdin.readline().split()))

sarr = set(arr)
sbrr = set(brr)

dap = list(sarr-sbrr)

if len(dap) == 0:
    print(0)
else :
    print(len(dap))
    dap.sort()

    for i in range(len(dap)):
        print(dap[i],end=" ")


