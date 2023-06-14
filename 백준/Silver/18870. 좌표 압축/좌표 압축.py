import sys

n=int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

a = set(arr)
a = list(a)
a.sort()

dic ={}

for i in range(len(a)):
    dic[a[i]] = i

for i in arr:
    print(dic[i],end= " ")