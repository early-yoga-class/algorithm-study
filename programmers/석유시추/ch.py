from collections import deque

def solution(land):
    answer = 0
    N = len(land)
    M = len(land[0])
    group = {}
    # 석유 연결된 값 모두 체크, 다음 행에도 존재하면 그것마저 더하기
    def bfs(x, y, visited):
        queue = deque()
        applyqueue = deque()
        applyqueue.append((x, y))
        queue.append((x, y))
        maxValue = 1
        visited[x][y] = True
        while queue:
            curX, curY= queue.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = dx + curX
                ny = dy + curY
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if visited[nx][ny]:
                    continue
                if land[nx][ny] == 0:
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
                applyqueue.append((nx, ny))
                maxValue += 1
                
        index = len(group) + 2
        group[index] = maxValue
        while applyqueue:
            curX, curY = applyqueue.popleft()
            land[curX][curY] = index
            
        
    visited = [[False] * M for _ in range(N)] 
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j, visited)
                
    for i in range(M):
        check = set()
        maxV = 0
        for j in range(N):
            if land[j][i] > 1 and land[j][i] not in check:
                maxV += group[land[j][i]]
                check.add(land[j][i])
        answer = max(answer, maxV)
            
    #가장 많은 석유량 뽑기
    return answer