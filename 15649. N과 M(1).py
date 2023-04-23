import sys
from itertools import permutations

a,b = map(int,sys.stdin.readline().split())
nums = []

for i in range(1,a+1,1):
    nums.append(i)

alist = list(permutations(nums,b))

for i in alist:
    print(' '.join(map(str,i)))
 