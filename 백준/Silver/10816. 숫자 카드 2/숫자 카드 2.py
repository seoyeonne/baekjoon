import sys

import sys

n = int(sys.stdin.readline())
nrr = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mrr = list(map(int,sys.stdin.readline().split()))

dic ={}

for i in mrr:
    dic[i] = 0


for j in nrr:
    if j in dic:
        dic[j] = dic[j] + 1
    else :
        dic[j] = 1

for i in range(m):
    if mrr[i] in dic:
        print(dic[mrr[i]],end=" ")
    else :
        print(0,end=" ")
