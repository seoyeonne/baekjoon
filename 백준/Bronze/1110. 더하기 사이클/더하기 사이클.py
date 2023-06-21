import sys

num = int(sys.stdin.readline())
M = num
num_kk = num
cnt = 0

while True:
    a = num//10
    b = num % 10
    c = (a + b) % 10
    num_kk = (b * 10) + c
    cnt = cnt + 1
    if num_kk == M :
        print(cnt)
        break
    else :
        num = num_kk
