import sys
from collections import deque

# N초가 흐른 후 격자판 상태
R, C, N = map(int, input().split())

board = [[str(n) for n in input()] for _ in range(R)]
timer_board = [[0] * C for _ in range(R)]

# 빈칸 .
# 폭탄 O

# 초기세팅
for i in range(R):
    for j in range(C):
        if board[i][j] == 'O':
            timer_board[i][j] = 3

time = 1
while 1:
    if time > N:
        break

     # 봄버맨 폭탄세팅
    if time >= 2 and time % 2 == 0:
        for i in range(R):
            for j in range(C):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    timer_board[i][j] = time + 3

    boom = []
    # 터지는 폭탄 체크
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                # 터지는 폭탄
                if timer_board[i][j] == time:
                    boom.append((i, j))


    for x, y in boom:
        board[x][y] = '.'
        timer_board[x][y] = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
            board[nx][ny] = '.'
            timer_board[nx][ny] = 0

    time += 1

for i in range(R):
    print("".join(list(map(str, board[i]))))