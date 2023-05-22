import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque([])

for _ in range(n):
    arr = sys.stdin.readline().split()
    if arr[0] == 'push' :
        deq.append(arr[1])
    elif arr[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else :
            print(deq[0])
    elif arr[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else :
            print(deq[-1])
    elif arr[0] == 'size':
        print(len(deq))
    elif arr[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else :
            print(0)
    else:
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)
