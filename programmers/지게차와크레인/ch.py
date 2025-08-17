from collections import deque

def solution(storage, requests):
    answer = 0
    # 4면중 적어도 1면이 창고 외부 연결
    
    # request = crane
    # 길이 1이면 지게차, 2이면 크레인
    # 2 <= n, m <= 50
    # 50 * 50 == 2500
    n = len(storage)
    m = len(storage[0])
    
    for i in range(n):
        storage[i] = list(ch for ch in storage[i])
        
    def bfs(x, y):
        queue = deque()
        visited = [[False] * m for _ in range(n)]
        visited[x][y] = True
        queue.append((x, y))
        while queue:
            curX, curY = queue.popleft()
            if curX < 0 or curY < 0 or curX >= n or curY >= m:
                return True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = dx + curX
                ny = dy + curY
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    return True
                if visited[nx][ny] : continue
                
                if storage[nx][ny] == 'e':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
            
        return False
    
    for request in requests:
        checkQueue = deque()
        # crane
        if len(request) == 2:
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == 'e': continue
                    if request[0] == storage[i][j]:
                        storage[i][j] = 'e'
                        answer += 1
        # 지게차
        else:
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == 'e': continue
                    if request[0] == storage[i][j]:
                        if bfs(i, j):
                            checkQueue.append((i, j))
                            
        for x, y in checkQueue:
            storage[x][y] = 'e'
            answer += 1
                    
                    
    return n * m - answer