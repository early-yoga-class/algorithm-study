import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())

answer = float('inf')

board = [[False] * (N + 1) for _ in range(H + 1)]

for i in range(M):
    a, b = map(int, input().split())
    board[a][b] = True

def can_ladder():
    for start in range(1, N + 1):
        y = start
        for x in range(1, H + 1):
            if board[x][y]:
                y += 1
            elif y > 1 and board[x][y - 1]:
                y -= 1
        if y != start:
            return False
    return True

def dfs(depth, x, y):
    global answer

    if can_ladder():
        answer = min(answer, depth)
        return
    if depth == 3 or depth >= answer:
        return

    for i in range(x, H + 1):
        for j in range(y if i == x else 1, N):
            if j >= N or board[i][j]: continue
            if j > 1 and board[i][j - 1]: continue
            if j < N - 1 and board[i][j + 1]: continue
            board[i][j] = True
            dfs(depth + 1, i, j + 2)
            board[i][j] = False

dfs(0, 1, 1)
print(answer if answer <= 3 else -1)