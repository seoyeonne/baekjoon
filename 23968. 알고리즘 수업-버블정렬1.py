import sys

n, k= map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

answer = -1

for i in range(n-1,0,-1):
    for j in range(i):
        if (arr[j]>arr[j+1]):
            k = k -1
            arr[j],arr[j+1] = arr[j+1],arr[j]

            if k == 0 :
                answer = f'{arr[j]} {arr[j+1]}'

print(answer)