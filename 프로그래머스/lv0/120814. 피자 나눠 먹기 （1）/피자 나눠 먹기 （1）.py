def solution(n):
    answer = 1
    while True :
        if n - 7 <= 0:
            return answer
            break
        else :
            answer = answer + 1
            n  = n - 7
