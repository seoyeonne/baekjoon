import sys

N = int(sys.stdin.readline())
arr = []
brr = []

for i in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)

print(round(sum(arr)/N))
arr.sort()
print(arr[N//2])

dic =dict()

for j in arr:
    if j in dic:
        dic[j] = dic[j] + 1
    else :
        dic[j] = 1

mx=max(dic.values())
mx_dic=[]

for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(arr) - min(arr))
