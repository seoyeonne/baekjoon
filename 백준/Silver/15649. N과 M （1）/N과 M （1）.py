import sys

N , M = map(int,sys.stdin.readline().split())
arr =[]

def back():
    if len(arr) == M :
        print(" ".join(map(str,arr)))

    for i in range(1,N+1):
        if i not in arr :
            arr.append(i)
            back()
            arr.pop()
    return

back()
