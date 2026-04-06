import sys
from collections import deque


# N 세로 M 가로
# 5 <= N, M <= 100
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
time = 0
melt_cheeses = deque([])
ex_air_ck = [[False] * M for _ in range(N)]


def init():
    global ex_air_ck
    ex_air_ck = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])
    ex_air_ck[0][0] = True
    while q:
        curX, curY = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = curX + dx
            ny = curY + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if ex_air_ck[nx][ny]: continue
            if board[nx][ny] == 1: continue
            ex_air_ck[nx][ny] = True
            q.append((nx, ny))

def find_melt_cheese():
    global melt_cheeses, ex_air_ck
    melt_flag = False
    for i in range(N):
        for j in range(M):
            if ex_air_ck[i][j]: continue
            air_cnt = 0
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = i + dx
                ny = j + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                if board[nx][ny] == 1: continue
                if not ex_air_ck[nx][ny]: continue
                # if air_cnt >= 2: break
                air_cnt += 1
            if air_cnt >= 2:
                melt_cheeses.append((i, j))
                melt_flag = True

    return melt_flag

def melt():
    global melt_cheeses
    while melt_cheeses:
        x, y = melt_cheeses.popleft()
        board[x][y] = 0


while True:
    init()
    if not find_melt_cheese():
        break

    melt()
    time += 1

print(time)