from collections import deque

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * n for _ in range(n)]
apartments = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    count = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1

    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = bfs(i, j)
            apartments.append(count)

apartments.sort()

print(len(apartments))
for count in apartments:
    print(count)