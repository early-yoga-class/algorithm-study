from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    col_result = [0] * m

    visited = [[False] * m for _ in range(n)]  
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True  
                count = 1
                
                # 지금 발견한 하나의 석유 덩어리가 걸쳐 있는 열 번호들을 기억해서,
                # 마지막에 그 열마다 덩어리 넓이(count)를 더해주는 용도
                # bfs돌면서 한 번 방문한 공간이면 그 덩어리가 포함된 열의 result에도 더해둠으로써 다시 방문할 필요 없음
                col = set()
                col.add(j)

                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True 
                                queue.append((nx, ny))
                                count += 1
                                col.add(ny)

                for c in col:
                    col_result[c] += count

    return max(col_result)
