from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
# result = ""

for i in range(m):
    v1, v2 = map(int, input().split())
    # 연결된 노드 표시
    graph[v1][v2] = 1 
    graph[v2][v1] = 1


def dfs(v, visited):
    # 방문 체크
    visited[v] = 1
    print(v, end=" ")
    
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i, visited)

def bfs(v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1


dfs(v, visited)
print()

visited = [0] * (n+1)
bfs(v, visited)
