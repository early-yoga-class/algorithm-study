from collections import deque

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
pipe = {
    1: [0,1,2,3], 2: [0,1], 3: [2,3], 4: [0,3],
    5: [1,3], 6: [1,2], 7: [0,2]
}
opposite = {0:1, 1:0, 2:3, 3:2}

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    q = deque()
    q.append((R, C, 1))    
    visited[R][C] = True
    count = 1

    while q:
        r, c, t = q.popleft()
        if t >= L:
            continue
        for d in pipe[grid[r][c]]:
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M): 
                continue
            if visited[nr][nc] or grid[nr][nc] == 0: 
                continue
          
            if opposite[d] not in pipe[grid[nr][nc]]:
                continue
            visited[nr][nc] = True
            count += 1
            q.append((nr, nc, t+1))
    print(f"#{tc} {count}")

