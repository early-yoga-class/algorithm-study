# 백준 2638번 치즈

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0

while True:
    outside = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    outside[0][0] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not outside[nx][ny] and board[nx][ny] == 0:
                    outside[nx][ny] = True
                    q.append((nx, ny))

    melt = []

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt = 0

                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]

                    if 0 <= ni < N and 0 <= nj < M:
                        if outside[ni][nj]:
                            cnt += 1

                if cnt >= 2:
                    melt.append((i, j))

    if not melt:
        break

    for x, y in melt:
        board[x][y] = 0

    time += 1

print(time)