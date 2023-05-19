import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    a_list = list(sys.stdin.readline().strip())
    stack = [a_list[0]]
    for j in range(1,len(a_list)):
        if len(stack) == 0:
            stack.append(a_list[j])
        else :
            if  a_list[j] == stack[-1]:
                stack.pop()
            else  :
                stack.append(a_list[j])

    if len(stack) == 0:
        cnt = cnt + 1

print(cnt)