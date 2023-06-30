import sys

def kaprekar(n):
    a_list = list(map(int,str(n)))
    num = sum(a_list) + n
    return num

lst = []
for i in range(1,10000):
    d = kaprekar(i)
    lst.append(d)
    if not i in lst:
        print(i)