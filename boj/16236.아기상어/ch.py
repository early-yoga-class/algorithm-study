import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

class BabyShark:
    def __init__(self, start_x, start_y):
        self.size = 2
        self.start_x = start_x
        self.start_y = start_y
        self.fish_count = 0
        self.time = 0

    def eat_fish(self, x, y, t):
        self.fish_count += 1
        if self.size == self.fish_count:
            self.size += 1
            self.fish_count = 0
        self.start_x = x
        self.start_y = y
        self.time += t

board = [list(map(int, input().split())) for _ in range(N)]

def move():
    x, y = baby_shark.start_x, baby_shark.start_y
    visited = [[False] * N for _ in range(N)]
    q = deque([])
    q.append((x, y, 0))
    visited[x][y] = True
    can_eat = []
    while q:
        curX, curY, dist = q.popleft()

        if 0 < board[curX][curY] < baby_shark.size:
            can_eat.append((dist, curX, curY))

        for dx, dy in [(-1, 0), (0 ,-1), (0, 1), (1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if visited[nx][ny]: continue
            if board[nx][ny] > baby_shark.size: continue
            q.append((nx, ny, dist + 1))
            visited[nx][ny] = True

    if len(can_eat) > 0:
        can_eat.sort(key=lambda x: (x[0], x[1], x[2]))
        dist, x, y = can_eat[0]
        baby_shark.eat_fish(x, y, dist)
        board[x][y] = 0
        return True
    else:
        return False

def init():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                board[i][j] = 0
                return BabyShark(i, j)

baby_shark = init()
while True:
    if not move():
        break

print(baby_shark.time)