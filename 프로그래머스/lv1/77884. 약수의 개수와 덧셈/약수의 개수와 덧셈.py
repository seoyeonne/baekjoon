def solution(left, right):
    answer = 0
    for i in range(left,right+1,1):
        cnt = []
        dap1 = []
        dap2 = []
        for j in range(1,i,1):
            if i % j == 0:
                cnt.append(j)
        if len(cnt) % 2 == 0:
            answer = answer + i
        else :
            answer = answer - i
    
    return abs(answer)