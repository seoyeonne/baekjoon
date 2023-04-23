import sys
from itertools import accumulate
#k 입력 숫자
#n 구하는 횟수

dap = []
brr = []
k,n = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

dap = list(accumulate(arr))
for i in range(n):
    sum = 0
    a,b = map(int,sys.stdin.readline().split())
    a = a-1
    b = b-1
    sum = dap[b] - dap[a] + arr[a]
    brr.append(sum)

for i in range(len(brr)):
    print(brr[i])