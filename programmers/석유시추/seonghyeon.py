from collections import deque
def solution(land):
    row = len(land)
    col = len(land[0])
    total = [0 for _ in range(col)]
    visited = [[0 for _ in range(col)] for _ in range(row)]
    queue = deque()

    def bfs(start, end):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        oil = 1
        visited[start][end] = 1
        queue.append([start, end])

        y_range = set([end])

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    oil += 1
                    queue.append([nx, ny])
                    y_range.add(ny)

        for i in y_range:
            total[i] += oil

    for i in range(row):
        for j in range(col):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j)

    return max(total)