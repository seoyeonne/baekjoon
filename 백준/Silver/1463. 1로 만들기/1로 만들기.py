import sys

n = int(sys.stdin.readline())
dap = [0 for i in range(n+1)]
dap[1] = 0

for i in range(2,n+1):
    dap[i] = dap[i-1] + 1
    if i%2 == 0:
        k = dap[i//2]+1
        if k< dap[i]:
            dap[i] = k
    if i%3 == 0:
        kk = dap[i//3] +1
        if kk< dap[i]:
            dap[i] = kk

print(dap[n])


