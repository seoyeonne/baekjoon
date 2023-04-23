
import operator
import sys
from collections import Counter

arr =[]
dap = []
n = int(sys.stdin.readline())

for i in range(n):
    book = str(sys.stdin.readline().replace('\n',' '))
    arr.append(book)

counter = Counter(arr)
counter_sort = sorted(counter.items(),key=lambda x:(-x[1],x[0]),reverse=True)


print(counter_sort[len(counter_sort)-1][0])
