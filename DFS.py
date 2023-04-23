import sys
sys.setrecursionlimit(10**6)


n,m,k = map(int,sys.stdin.readline().split())
#방문 배열
visited = [False]*(n+1)
#입력 그래프
tree = [[] for _ in range(n+1)]
#부모노드 저장 리스트
answer = [0]*(n+1)
cnt=1

for i in range(n):#인접리스트로 저장
    n1,n2 = map(int,sys.stdin.readline().split())
    #양방향 저장
    tree[n1].append(n2)
    tree[n2].append(n1)

#DFS
def DFS(number):
    global cnt
    visited[number] = True

    answer[number] = cnt
    tree[number].sort()
    for i in tree[number]:
        if not visited[i]:
            cnt = cnt + 1
            DFS(i)

DFS(1)

for i in range(len(answer)):
    print(answer[i])