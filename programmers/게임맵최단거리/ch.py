from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 1))
        visited[x][y] = True
        
        while queue:
            curX, curY, moves= queue.popleft()
            if curX == n - 1 and curY == m - 1:
                return moves
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = dx + curX
                ny = dy + curY
                if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
                if visited[nx][ny]: continue
                if maps[nx][ny] == 0: continue
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))
        return -1
        
    return bfs(0, 0)