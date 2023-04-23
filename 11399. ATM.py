import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dap = [0 for i in range(N+1)]

arr.sort()

for i in range(0,len(arr),1):
    dap[i+1] = dap[i] + arr[i]


print(sum(dap))

#삽입 정렬로 구현
for i in range(1,N):
    insert_point = i
    insert_value = arr[i]
    for j in range(i-1,-1,-1):
        if arr[j] < arr[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i,insert_point,-1):
        arr[j] = arr[j-1]
    arr[insert_point] = insert_value

