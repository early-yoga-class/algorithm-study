from collections import deque
    
def solution(maps):
    m = len(maps) # 행
    n = len(maps[0]) # 열
    visited = [[0]*(n) for i in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    visited[0][0] = 1
    queue.append((0, 0)) # (0, 0) ~ (n-1, m-1)

    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if (0 <= nx < m) and (0 <= ny < n):
                if (maps[nx][ny] == 1) and (visited[nx][ny] == 0):
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    queue.append((nx, ny))

    if visited[m-1][n-1] == 0:
        return -1
    else:
        return visited[m-1][n-1]