import sys

arr= [0 for i in range(30)]
for i in range(28):
    n = int(sys.stdin.readline())
    arr[n-1] = 1

for i in range(len(arr)):
    if arr[i] !=1 :
        print(i+1)
