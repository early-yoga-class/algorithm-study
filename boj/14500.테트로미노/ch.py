import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

tetrominos = [
    # I (2)
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    # ㅁ (1)
    [(0, 1), (1, 0), (1, 1)],
    # ㄴ/ㄱ (8)
    [(1, 0), (2, 0), (2, 1)],
    [(1, 0), (2, 0), (2, -1)],
    [(0, 1), (1, 0), (2, 0)],
    [(0, -1), (1, 0), (2, 0)],
    [(0, 1), (0, 2), (1, 2)],
    [(0, 1), (0, 2), (-1, 2)],
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (0, 2), (-1, 0)],
    # S/Z (4)
    [(0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (1, -1)],
    [(1, 0), (1, -1), (2, -1)],
    # ㅗ (4)
    [(0, -1), (0, 1), (1, 0)],     # ㅗ
    [(0, -1), (0, 1), (-1, 0)],    # ㅜ
    [(-1, 0), (1, 0), (0, 1)],     # ㅏ
    [(-1, 0), (1, 0), (0, -1)],    # ㅓ
]


def solve(idx, startX, startY, count, total):
    global answer

    if count == len(tetrominos[idx]):
        if total > answer:
            answer = total
        return

    dx, dy = tetrominos[idx][count]
    nx = startX + dx
    ny = startY + dy
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return
    solve(idx, startX, startY, count + 1, total + board[nx][ny])

answer = 0
for i in range(N):
    for j in range(M):
        for type in range(len(tetrominos)):
            solve(type, i, j, 0, board[i][j])

print(answer)