import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

arr = []
for i in range(1,N+1,1):
    arr.append(i)

deq = deque(arr)

while len(deq) !=1 :
    deq.popleft()
    deq.append(deq[0])
    deq.popleft()

print(deq[0])

