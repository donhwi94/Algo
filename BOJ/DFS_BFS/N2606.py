from collections import deque

computer_num = int(input())
m = int(input())

graph = [[0] * (computer_num + 1) for _ in range(computer_num + 1)]
visited = [0] * (computer_num + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

count = 0

def bfs(v, visited):
    global count
    queue = deque()
    queue.append(v)
    visited[v] = 1
    
    while queue:
        v = queue.popleft()
        count += 1

        for i in range(1, computer_num+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

bfs(1, visited)

# 1번 컴퓨터 제외
print(count - 1)