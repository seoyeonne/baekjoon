import sys
from collections import deque

while True:
    try:
        s, t = input().split()
        queue = deque(list(s))

        for c in t:
            if queue and c == queue[0]:
                queue.popleft()

        if queue:
            print('No')
        else:
            print('Yes')
    except:
        break