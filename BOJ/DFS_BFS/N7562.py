import sys
from collections import deque

tc = int(sys.stdin.readline().rstrip())

# 나이트가 이동할 수 있는 범위
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
            

for _ in range(tc):
    length = int(sys.stdin.readline().rstrip())
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    graph = [[0] * length for _ in range(length)]
    
    if start_x == end_x and start_y == end_y:
        print(0)
        continue
    
    print(bfs(start_x, start_y))
