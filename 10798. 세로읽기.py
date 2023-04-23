import sys

arr = [[0]*15 for i in range(5)]

for i in range(5):
    d = list(input())
    d_len = len(d)
    for j in range(d_len):
        arr[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if (arr[j][i] == 0):
            continue
        else :
            print(arr[j][i],end="")