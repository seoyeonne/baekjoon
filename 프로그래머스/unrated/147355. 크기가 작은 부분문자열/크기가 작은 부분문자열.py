
def solution(t, p):
    cnt = 0
    arr = []
    dap = []
    for i in range(0,len(t)-len(p)+1):
        arr.append(t[i:i+len(p)])
    for j in range(len(arr)):
        if arr[j] <= p :
            cnt = cnt + 1
            
    return cnt
