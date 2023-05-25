import math

def solution(price):
    if price >= 500000: 
        discount = 0.2
    elif price >= 300000:
        discount = 0.1
    elif price >= 100000:
        discount = 0.05
    else:
        discount = 0
    answer = math.floor(price * (1 - discount))
    return answer