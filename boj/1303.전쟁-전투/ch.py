import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [[_ for _ in input().strip()] for _ in range(M)]

# bfs
def bfs(x, y, color):
    q = deque([])
    visited[x][y] = True
    q.append((x, y))
    cnt = 1
    while q:
        curX, curY = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = curX + dx
            ny = curY + dy
            if nx < 0 or ny < 0 or nx >= M or ny >= N: continue
            if visited[nx][ny]: continue
            if board[nx][ny] != color: continue
            q.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1

    if color == 'W': answer[0] += cnt * cnt
    else: answer[1] += cnt * cnt

        # W, B
answer = [0, 0]
visited = [[False] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, board[i][j])

print(answer[0], answer[1])