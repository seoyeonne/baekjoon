import sys
import math

def check (x):
    if(x==1):
        return True
    for j in range(2,int(math.sqrt(x))+1, 1):
        if (x % j == 0):
            return True
    return False


n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
cnt = 0

for i in range(len(arr)):
    if (check(arr[i])==False):
        cnt = cnt + 1
print(cnt)