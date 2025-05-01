from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[[False]*4 for _ in range(n)] for _ in range(m)]

nowX, nowY, nowD = map(int, input().split())
nowX -= 1; nowY -= 1; nowD -= 1
goalX, goalY, goalD = map(int, input().split())
goalX -= 1; goalY -= 1; goalD -= 1

direction = [[0,1], [0,-1], [1,0], [-1,0]]

leftDir  = [3, 2, 0, 1]
rightDir = [2, 3, 1, 0]

queue = deque()
visited[nowX][nowY][nowD] = True
queue.append([nowX, nowY, nowD, 0])

def bfs():
    while queue:
        x, y, d, cost = queue.popleft()

        if x == goalX and y == goalY and d == goalD:
            print(cost)
            return

        for i in range(1, 4):
            nx = x + direction[d][0] * i
            ny = y + direction[d][1] * i

            if not (0 <= nx < m and 0 <= ny < n) or board[nx][ny] == 1:
                break

            if not visited[nx][ny][d]:
                visited[nx][ny][d] = True
                queue.append([nx, ny, d, cost + 1])

        for nd in (leftDir[d], rightDir[d]):
            if not visited[x][y][nd]:
                visited[x][y][nd] = True
                queue.append([x, y, nd, cost + 1])

bfs()