import sys
from collections import deque

wheel_types = [[int(num) for num in input().strip()] for _ in range(4)]

def rotate(number, direction):
    dq = deque(wheel_types[number])
    dq.rotate(direction)
    return list(dq)

def bfs(number, direction):
    q = deque()
    visited = [False] * 4
    dirs = [0] * 4
    q.append((number, direction))
    visited[number] = True
    current_status = [w[:] for w in wheel_types]
    dirs[number] = direction
    while q:
        curr, curr_dir = q.popleft()

        nx = curr - 1
        if 0 <= nx < 4:
            if not visited[nx]:
                if current_status[nx][2] != current_status[curr][6]:
                    q.append((nx, -1 * curr_dir))
                    visited[nx] = True
                    dirs[nx] = -curr_dir

        nx = curr + 1
        if 0 <= nx < 4:
            if not visited[nx]:
                if current_status[nx][6] != current_status[curr][2]:
                    q.append((nx, -1 * curr_dir))
                    visited[nx] = True
                    dirs[nx] = -curr_dir

    for i in range(4):
        if dirs[i] != 0:
            wheel_types[i] = rotate(i, dirs[i])


K = int(input())
for i in range(K):
    number, direction = map(int, input().split())
    bfs(number - 1, direction)

answer = 0
for i in range(4):
    answer += (2 ** i) * wheel_types[i][0]
print(answer)