import sys
# 최소공배수는 a*b/최대공약수 -> 위클리드 호제법으로 최대공약수 구한 후
# 최소공배수 구할 수 있음
n = int(sys.stdin.readline())

def gcd(a,b):
    #여기서 b로 들어오는 값은 a%b
    if b == 0:
        #여기서 a는 b값이 들어옴
        return a
    else :
        return gcd(b,a%b)



for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if(a<b):
        tmp = a
        a = b
        b = tmp
    result = a * b // gcd(a,b)
    print(result)