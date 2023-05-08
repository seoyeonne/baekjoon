import sys

arr = []

for i in range(9):
    arr.append(list(map(int,sys.stdin.readline().split())))

tmp = arr[0][0]
b = ''

for i in range(9):
    for j in range(9):
        if tmp <= arr[i][j]:
            tmp = arr[i][j]
            b = str(i+1) + ' ' + str(j+1)

print(tmp)
print(b)