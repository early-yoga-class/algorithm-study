# 백준 20608번 상어초등학교

import sys
input = sys.stdin.readline

n = int(input().strip())
order = []
like = {}
for _ in range(n * n):
    a, b, c, d, e = map(int, input().split())
    order.append(a)
    like[a] = {b, c, d, e}

board = [[0] * n for _ in range(n)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def count_around(x, y, s):
    lcnt = 0
    ecnt = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                ecnt += 1
            elif board[nx][ny] in s:
                lcnt += 1
    return lcnt, ecnt

for student in order:
    best = (-1, -1, n, n)
    s = like[student]
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue
            lcnt, ecnt = count_around(i, j, s)
            if (lcnt > best[0] or
                (lcnt == best[0] and ecnt > best[1]) or
                (lcnt == best[0] and ecnt == best[1] and (i < best[2] or (i == best[2] and j < best[3])))):
                best = (lcnt, ecnt, i, j)
    board[best[2]][best[3]] = student

score_map = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
ans = 0
for i in range(n):
    for j in range(n):
        s = like[board[i][j]]
        cnt = 0
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < n and 0 <= nj < n and board[ni][nj] in s:
                cnt += 1
        ans += score_map[cnt]

print(ans)
