import sys
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline())
#방문 배열
visited = [False]*(n+1)
#입력 그래프
tree = [[] for _ in range(n+1)]
#부모노드 저장 리스트
answer = [0]*(n+1)

for i in range(1,n):#인접리스트로 저장
    n1,n2 = map(int,sys.stdin.readline().split())
    #양방향 저장
    tree[n1].append(n2)
    tree[n2].append(n1)

#DFS
def DFS(number):
    visited[number] = True
    for i in tree[number]:
        if not visited[i]:
            answer[i] = number
            DFS(i)

DFS(1)

for i in range(2,n+1):
    print(answer[i])