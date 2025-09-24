import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 2

L = int(input())
info = []
for _ in range(L):
    sec, direction = input().split()
    info.append((int(sec), direction))

snake = deque([(1,1)])

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

idx = 0
time = 0

for i in range(L):
    sec, direction = info[i]

    while time < sec:
        head_x, head_y = snake[0]
        nx, ny = head_x + dx[idx], head_y + dy[idx]

        # 벽 충돌
        if not (1 <= nx <= N and 1 <= ny <= N):
            print(time + 1)
            sys.exit(0)

        # 몸 충돌 (꼬리 예외 처리)
        apple = (board[nx][ny] == 2)
        tail = snake[-1]
        body_hit = (nx, ny) in snake and not ((not apple) and (nx, ny) == tail)
        if body_hit:
            print(time + 1)
            sys.exit(0)

        # 이동
        snake.appendleft((nx, ny))
        if apple:
            board[nx][ny] = 0
        else:
            snake.pop()

        # 시간 증가 후, 해당 초 이동이 끝났다면 회전 적용
        time += 1
        if time == sec:
            if direction == "L":
                idx = (idx + 3) % 4
            else:  # "D"
                idx = (idx + 1) % 4

# 모든 회전 처리 후에도 부딪힐 때까지 계속 전진
while True:
    head_x, head_y = snake[0]
    nx, ny = head_x + dx[idx], head_y + dy[idx]

    if not (1 <= nx <= N and 1 <= ny <= N):
        print(time + 1)
        sys.exit(0)

    apple = (board[nx][ny] == 2)
    tail = snake[-1]
    body_hit = (nx, ny) in snake and not ((not apple) and (nx, ny) == tail)
    if body_hit:
        print(time + 1)
        sys.exit(0)

    snake.appendleft((nx, ny))
    if apple:
        board[nx][ny] = 0
    else:
        snake.pop()

    time += 1
