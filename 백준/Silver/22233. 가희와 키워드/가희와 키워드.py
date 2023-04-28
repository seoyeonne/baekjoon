import sys

dic = {}
res1 = []
n,m = map(int,sys.stdin.readline().split())

for i in range(n):
    dic[sys.stdin.readline().rstrip()] = 1

res = n

for _ in range(m):
    word = sorted(sys.stdin.readline().rstrip().split(','))

    for t in word:
        if t in dic.keys():
            if dic[t] == 1:
                dic[t] = dic[t] -1
                res = res -1
    res1.append(res)

for i in range(len(res1)):
    print(res1[i])