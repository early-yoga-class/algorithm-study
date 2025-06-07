import heapq

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dp = [[float('inf')]*m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = []
    heapq.heappush(q,(0,0))
    dp[0][0] = 1
    while q:
        x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if maps[nx][ny] == 0:
                continue
            if dp[nx][ny] > dp[x][y] + 1:
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + 1)
                heapq.heappush(q,(nx,ny))

    if dp[n-1][m-1] == float('inf'):
        return -1
    else:
        return dp[n-1][m-1]

