from collections import deque
    
def solution(land):
    global result, visited
    def check(i,j):
        global result
        count = 0
        di = [1,-1,0,0]
        dj = [0,0,1,-1]
        visited[i][j] = True
        visit_col = set([j])
        queue = deque()
        queue.append((i,j))
        while queue:
            i, j = queue.popleft()
            count +=1
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m and land[ni][nj] == 1 and not visited[ni][nj]:
                    queue.append((ni,nj))  
                    visited[ni][nj] = True
                    visit_col.add(nj)
        for i in visit_col:
                result[i] +=count
            
        return count

    n = len(land)
    m = len(land[0])
    result = [0] * m

    visited = [[False]*(m) for _ in range(n)]
    
    for j in range(m):
        for i in range(n):
            if land[i][j] == 1 and not visited[i][j]:
                check(i,j)
    answer = max(result)
    return answer
