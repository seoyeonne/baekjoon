arr = []
n = int(input())

for i in range(n):
    arr = list(map(str, input().split()))
    for j in range(len(arr)):
        brr = []
        brr = list(arr[j])
        brr.reverse()
        for k in range(len(brr)):
            print(brr[k],end="")
        print(" ",end="")