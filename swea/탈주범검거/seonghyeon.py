
from collections import deque

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

direction = list()
direction.append([])
direction.append([True, True, True, True])
direction.append([True, False, True, False])
direction.append([False, True, False, True])
direction.append([True, False, False, True])
direction.append([False, False, True, True])
direction.append([False, True, True, False])
direction.append([True, True, False, False])


def bfs(queue, board, direction, visited):
    global count
    size = len(queue)
    limit = 0
    while (queue and limit != size):
        limit += 1
        x, y = queue.popleft()
        direct = direction[board[x][y]]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if board[nx][ny] == 0:
                    continue
                nDirection = direction[board[nx][ny]]
                if direct[i] == False:
                    continue
                elif direct[i] and nDirection[(i+2)%4]:
                    if visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    count += 1
                    queue.append([nx, ny])


for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    count = 0

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()
    visited[R][C] = True
    count += 1
    timelimit = 1
    queue.append([R, C])

    while timelimit != L:
        bfs(queue, board, direction, visited)
        timelimit += 1

    result = f'#{test_case} {count}'
    print(result)