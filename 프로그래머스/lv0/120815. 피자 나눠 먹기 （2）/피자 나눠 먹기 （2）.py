#find 최소공배수  a * b //gcd

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


def solution(n):
    answer = 0
    gcd1 = 0
    gcd1 = gcd(n,6)
    answer = (n * 6 // gcd1) // 6
    return answer