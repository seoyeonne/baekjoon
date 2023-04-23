import sys

a,b = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
brr = list(map(int,sys.stdin.readline().split()))

arr = set(arr)
brr = set(brr)

print(len(arr-brr)+len(brr-arr))