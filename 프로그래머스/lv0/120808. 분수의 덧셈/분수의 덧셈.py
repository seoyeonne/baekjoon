
def solution(numer1, denom1, numer2, denom2):
    answer = []
    dap_numer = 0
    dap_denom = 0
    dap_numer = (numer1 * denom2) + (numer2 * denom1)
    dap_denom = (denom1 * denom2)
    gcd1 = gcd(dap_numer,dap_denom)
    
    if gcd == 1:
        answer.append(dap_numer)
        answer.append(dap_denom)
    else :
        answer.append(dap_numer//gcd1)
        answer.append(dap_denom//gcd1)
    
    return answer

def gcd(dap_numer,dap_denom):
    if dap_denom == 0:
        return dap_numer
    else :
        return gcd(dap_denom,dap_numer%dap_denom)
