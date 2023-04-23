
arr = []
while 1:
    n=int(input())
    if n==-1:
        break
    else:
        arr.append(n)

for i in range(len(arr)):
    sum = 0
    brr = []
    for j in range(1,arr[i],1):
        if arr[i]%j == 0:
            brr.append(j)
            sum = sum + j
        else :
            j = j+1
    if sum == arr[i]:
        b = ' + '.join(map(str, brr))
        print(arr[i], '=', b)
    else:
        print(arr[i], 'is NOT perfect.')
