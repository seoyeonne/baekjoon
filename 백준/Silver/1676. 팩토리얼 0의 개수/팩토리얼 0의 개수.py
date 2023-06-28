import sys

def fac(n):
    if n ==0 or n==1 :
        return 1
    else :
        return n * fac(n-1)


cnt = 0
facc = 1

n = int(sys.stdin.readline())

facc = str(fac(n))

for i in facc[::-1]:
    if i == '0':
        cnt = cnt + 1
    else :
        print(cnt)
        break