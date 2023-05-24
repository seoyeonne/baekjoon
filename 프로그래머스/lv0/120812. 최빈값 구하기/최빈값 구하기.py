from collections import Counter
def solution(array):
    answer = ''
    counter = Counter(array)
    
    most_common = counter.most_common()
    
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        answer = -1
    else :
        answer = most_common[0][0]
    return answer