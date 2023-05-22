def gcd(n,m):
    if m == 0:
        return n
    else :
        return gcd(m,n%m)


def solution(n, m):
    answer = []
    a = gcd(n,m)
    answer.append(a)
    b = n * m // gcd(n,m)
    answer.append(b)
    return answer