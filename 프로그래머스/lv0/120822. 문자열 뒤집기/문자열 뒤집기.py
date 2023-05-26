def solution(my_string):
    answer = ' '
    my = list(my_string)
    my.reverse()
    answer = ''.join(my)
    return answer