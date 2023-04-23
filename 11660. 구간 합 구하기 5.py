from sys import stdin

n,k = map(int, stdin.readline().split())

arr = [[0] * (n+1)]
brr = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
  arr_row = [0] + [int(x) for x in input().split()]
  arr.append(arr_row)

for i in range(1,n+1):
  for j in range(1,n+1):
    brr[i][j] = brr[i][j-1] + brr[i-1][j] - brr[i-1][j-1] + arr[i][j]

print(brr)
for i in range(k):
  a,b,c,d = map(int, stdin.readline().split())
  result = brr[c][d] - brr[a-1][d] - brr[c][b-1] + brr[a-1][b-1]
  print(result)