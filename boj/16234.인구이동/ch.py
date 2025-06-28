import math
import sys
from collections import deque


input = sys.stdin.readline

N, L, R = map(int, input().split())

board = [[int(num) for num in input().split()] for _ in range(N)]


def bfs(x, y, visited):
    inner_flag = False
    queue = deque()
    queue.append((x, y))
    sumQueue = deque()
    sumQueue.append((x, y))
    visited[x][y] = True
    while queue:
        curX, curY = queue.popleft()
        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if visited[nx][ny]: continue
            dif = abs(board[nx][ny] - board[curX][curY])
            if dif < L or dif > R or dif <= 0: continue
            visited[nx][ny] = True
            queue.append((nx, ny))
            sumQueue.append((nx, ny))
            inner_flag = True

    # 인구이동 시작
    if inner_flag == True:
        union_person = 0
        union_country = len(sumQueue)
        for x, y in sumQueue:
            union_person += board[x][y]

        move_person = math.floor(union_person / union_country)
        for x, y in sumQueue:
            board[x][y] = move_person

    return inner_flag

flag = True
time = 0

while True:
    # 모두 L <= R이나 같은 값으로 통일일 경우 or 한칸도 이동할 곳이 없을겨우
    if not flag:
        break

    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 인구이동이 가능한 칸이
            if not visited[i][j]:
                if bfs(i, j, visited):
                    flag = True
    if flag:
        time += 1

print(time)