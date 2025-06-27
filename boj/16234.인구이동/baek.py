from collections import deque
from copy import deepcopy

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

days = 0

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    united = [(x, y)]
    total_pop = country[x][y]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(country[cx][cy] - country[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    united.append((nx, ny))
                    total_pop += country[nx][ny]

    if len(united) > 1:
        new_pop = total_pop // len(united)
        for ux, uy in united:
            country[ux][uy] = new_pop
        return True
    return False

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True

    if not moved:
        break
    days += 1

print(days)
