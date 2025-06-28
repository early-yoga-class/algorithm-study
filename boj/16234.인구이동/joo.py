import sys
from collections import deque
n, l, r = (map(int, sys.stdin.readline().split()))

a = []
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))



# dir = [(1,0),(0,1),(-1,0),(0,-1)]


dx = (-1,1,0,0)
dy = (0,0,1,-1)
q = deque()
day = 0

while True:
    visited = [[False]*n for _ in range(n)]
    moved = False

    
    for rr in range(n):
        for c in range(n):
            if not visited[rr][c] :
                #q = deque([(rr,c)])
                q.clear()
                q.append((rr,c))
                visited[rr][c] = True
                mem = [(rr,c)]
                total_pop = a[rr][c]
                while q:
                    x, y = q.popleft()
                    # for dx,dy in dir:
                    #     nx , ny = x + dx, y +dy
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0<=nx < n and 0<=ny < n and not visited[nx][ny]:
                            if l <= abs(a[x][y] - a[nx][ny]) <= r:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                mem.append((nx,ny))
                                total_pop += a[nx][ny]
                if (len(mem) >= 2):
                    avg_pop = total_pop // len(mem)
                    moved = True
                    for (o,p) in mem:
                        a[o][p] = avg_pop

    
    if not moved:
        break
    day += 1
print(day)





