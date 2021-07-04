from collections import deque

n, m, k, x = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
# graph = [[] for _ in range(n+1)] # 인접 리스트로 표현
visited = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    # 인접 행렬로 표현 
    graph[a][b] = 1
    # 인접 리스트로 표현
    # graph[a].append(b)

def dfs(v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = 0

    while queue:
        v = queue.popleft()
        for i in range(1, n+1):
            if graph[v][i] == 1:
                queue.append(i)
                distance = visited[v] + 1
                if visited[i] == -1:
                    visited[i] = distance

dfs(x, visited)

num_null = True
for i in range(1, n+1):
    if visited[i] == k:
        num_null = False
        print(i)

if num_null == True:
    print(-1)