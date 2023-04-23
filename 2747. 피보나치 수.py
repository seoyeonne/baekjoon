import sys

n = int(sys.stdin.readline())
if n<=45:
    ph=[0,1]
    for i in range(n-1):
        ph.append(ph[i]+ph[i+1])
    print(ph[-1])