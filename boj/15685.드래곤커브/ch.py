import sys
# 동, 북, 서, 남
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

board = [[0] * 101 for _ in range(101)]

N = int(input())

for i in range(N):
    # 시작점, 시작방향, 세대
    y, x, d, g = map(int, input().split())
    dir_q = [d]

    for _ in range(g):
        for direction in reversed(dir_q):
            dir_q.append((direction + 1) % 4)

    board[x][y] = 1

    cur_x, cur_y = x, y
    for direction in dir_q:
        dx, dy = directions[direction]
        cur_x += dx
        cur_y += dy
        board[cur_x][cur_y] = 1


answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] != 1: continue
        if board[i][j] == 1 and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
            answer += 1

print(answer)