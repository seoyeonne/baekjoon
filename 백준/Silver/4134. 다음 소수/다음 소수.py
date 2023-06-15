import sys,math

#소수 판별 함수
def nums(num):
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1,1):
            if num%i == 0:
                return False
        return True

n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    while True:
        if nums(a):
            print(a)
            break
        else :
            a = a + 1
