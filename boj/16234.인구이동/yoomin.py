import math
import sys
from collections import deque

N, L, R = map(int,sys.stdin.readline().split())
population = []
queue = deque()
for _ in range(N):
    population.append(list(map(int,sys.stdin.readline().split())))
dx = [-1,1,0,0]
dy = [0,0,1,-1]
day = 0

while(True):
    check = False
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                union = []
                queue.append((i,j))
                cnt = 0
                total = 0
                while queue:
                    x, y = queue.popleft()
                    union.append((x,y))
                    cnt += 1
                    total += population[x][y]
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<= nx < N and 0<= ny < N and not visited[nx][ny]:
                            if L <= abs(population[x][y] - population[nx][ny]) <=R:
                                queue.append((nx,ny))
                                visited[nx][ny] = True                   

                if cnt != 1:
                    for x,y in union:
                        avg = math.floor(total/cnt)
                        population[x][y] = avg
                        check = True
    if check == False:
        break
    else:
        day += 1

print(day)