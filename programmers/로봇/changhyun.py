import sys
from collections import deque

input = sys.stdin.readline


# Go k = 1, 2, 3 k칸 움직일 수 있다.
# Turn dir = left, right

n, m = map(int, input().split())
visited = [[[False] * 4 for _ in range(m)] for _ in range(n)] # 방향 다른 방문체크도 필요
maps = [[int(num) for num in input().split()] for _ in range(n)]

startX, startY, startDir = map(int, input().split())
endX, endY, endDir = map(int, input().split())
direction = [(-1,0),(0,1),(1,0),(0,-1)] # left, right 돌릴 수 있는 순서

fixDir = [0, 1, 3, 2] # 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4이므로 시작 방향 수정
startDir = fixDir[startDir % 4]
endDir   = fixDir[endDir % 4]
ans = 10**9

queue = deque()
queue.append((startX - 1, startY - 1, startDir, 0))
visited[startX - 1][startY - 1][startDir] = True
while queue:
    currX, currY, currDir, cnt = queue.popleft()
    if currX == endX - 1 and currY == endY - 1 and currDir == endDir:
        print(cnt)
        break

    # 왼쪽, 오른쪽 방향들 체크
    right = (currDir + 1) % 4
    if not visited[currX][currY][right]:
        visited[currX][currY][right] = True
        queue.append((currX, currY, right, cnt + 1))

    left = (currDir + 3) % 4
    if not visited[currX][currY][left]:
        visited[currX][currY][left] = True
        queue.append((currX, currY, left, cnt + 1))

    dx, dy = direction[currDir]
    # 1, 2, 3 step 체크
    for k in range(1, 4):
        nx = currX + dx * k
        ny = currY + dy * k
        if nx < 0 or ny < 0 or nx >= n or ny >= m or maps[nx][ny] == 1: break
        if not visited[nx][ny][currDir]:
            visited[nx][ny][currDir] = True
            queue.append((nx, ny, currDir, cnt + 1))