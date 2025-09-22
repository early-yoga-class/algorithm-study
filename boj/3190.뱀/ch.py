import sys
from collections import deque

N = int(input())
board = [[0 for _ in range(N + 1)]for _ in range(N + 1)]
K = int(input())
apples = set()
for i in range(K):
    x, y = map(int, input().split())
    apples.add((x, y))

L = int(input())
turns = deque([])
for i in range(L):
    num, direction = input().split()
    turns.append((int(num), direction))


# 우, 하, 좌, 상 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
head_dir = 0
body = deque([(1, 1)])
time = 0
while True:
    # 방향 전환
    if turns and time == turns[0][0]:
        temp, turn_dir = turns.popleft()
        if turn_dir == 'D':
            head_dir = (head_dir + 1) % 4
        else:
            head_dir = (head_dir - 1) % 4

    nx = body[-1][0] + dx[head_dir]
    ny = body[-1][1] + dy[head_dir]

    # 범위 밖이면
    if nx <= 0 or ny <= 0 or nx > N or ny > N: break
    if (nx, ny) in body: break

    body.append((nx, ny))

    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        body.popleft()

    time += 1

print(time + 1)