# 백준 1303번 전쟁 - 전투

from collections import deque

N, M = map(int, input().split())
war = []
visit = [[False]*N for i in range(M)]
count_W = []
count_B = []
for i in range(M):
    war.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(x, y):
    if visit[x][y] != True:
        count = 1
        temp = war[x][y]
        visit[x][y] = True
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                now_x, now_y = x + dx[i], y + dy[i]
                if 0 <= now_x < M and 0 <= now_y < N:
                    if war[now_x][now_y] == temp and visit[now_x][now_y] != True:
                        count += 1
                        visit[now_x][now_y] = True
                        queue.append((now_x,now_y))
        
        if temp == "W":
            count_W.append(count)
        else:
            count_B.append(count)

for i in range(M):
    for j in range(N):
        check(i, j)

print(f'{sum(i**2 for i in count_W)} {sum(i**2 for i in count_B)}')