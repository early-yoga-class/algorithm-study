import math
import sys
from collections import deque

input = sys.stdin.readline

R, C, T = map(int,input().split())

board = [list(map(int, input().split())) for _ in range(R)]

def spread():
    spread_board = [[0] * C for _ in range(R)]

    q = deque([])
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                q.append((i, j))

    while q:
        curX, curY = q.popleft()

        can_spread_cnt = 0
        can_spread = []
        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY

            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
            if board[nx][ny] == -1: continue
            can_spread.append((nx, ny))
            can_spread_cnt += 1

        spread_amount = board[curX][curY] // 5
        for x, y in can_spread:
            spread_board[x][y] += spread_amount
        board[curX][curY] = board[curX][curY] - spread_amount * can_spread_cnt

    for i in range(R):
        for j in range(C):
            board[i][j] += spread_board[i][j]


def air_clear(x, y):
    moves = deque([])
    moves.extend(board[x][1:])
    moves.extend(board[_][C - 1] for _ in range(x - 1, 0, -1))
    moves.extend(reversed(board[0]))
    moves.extend(board[_][0] for _ in range(1, x))
    moves.appendleft(0)
    moves.pop()

    for i in range(1, C):
        board[x][i] = moves.popleft()
    for i in range(x - 1, -1, -1):
        board[i][C - 1] = moves.popleft()
    for i in range(C - 2, -1, -1):
        board[0][i] = moves.popleft()
    for i in range(1, x):
        board[i][0] = moves.popleft()

    moves = deque([])
    moves.extend(board[x + 1][1:])  # →
    moves.extend(board[i][C - 1] for i in range(x + 2, R))  # ↓
    moves.extend(board[R - 1][i] for i in range(C - 2, -1, -1))  # ←
    moves.extend(board[i][0] for i in range(R - 2, x + 1, -1))  # ↑
    moves.appendleft(0)
    moves.pop()

    for i in range(1, C):
        board[x + 1][i] = moves.popleft()
    for i in range(x + 2, R):
        board[i][C - 1] = moves.popleft()
    for i in range(C - 2, -1, -1):
        board[R - 1][i] = moves.popleft()
    for i in range(R - 2, x + 1, -1):
        board[i][0] = moves.popleft()


def find_air_purifier():
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                return i, j

air_purifier = find_air_purifier()

for _ in range(T):
    spread()
    air_clear(air_purifier[0], air_purifier[1])

print(sum(sum(i) for i in board) + 2)