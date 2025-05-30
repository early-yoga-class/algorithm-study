from collections import deque
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    ans = 0

    def is_connected(nx, ny, curX, curY):
        # 둘이 연결되었는지 체크해야한다.
        for dx,dy in pipe_check(maps[nx][ny]):
            prevX = nx + dx
            prevY = ny + dy
            if prevX == curX and prevY == curY:
                return True
        return False

    def pipe_check(number):
        if number == 1:
            return [(0, 1), (0, -1), (1, 0), (-1, 0)]
        elif number == 2:
            return [(-1, 0), (1, 0)]
        elif number == 3:
            return [(0, 1), (0, -1)]
        elif number == 4:
            return [(-1, 0), (0, 1)]
        elif number == 5:
            return [(1, 0), (0, 1)]
        elif number == 6:
            return [(1, 0), (0, -1)]
        else:
            return [(-1, 0), (0, -1)]


    def bfs(x, y):
        global ans
        queue = deque()
        queue.append((x, y, 1))
        visited[x][y] = True
        while queue:
            curX, curY, time = queue.popleft()
            if time >= L: continue
            direct = pipe_check(maps[curX][curY])
            for dx, dy in direct:
                nx = dx + curX
                ny = dy + curY
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                if visited[nx][ny]: continue
                if maps[nx][ny] == 0: continue
                if not is_connected(nx, ny, curX, curY): continue
                queue.append((nx, ny, time + 1))
                visited[nx][ny] = True
                ans += 1


    bfs(R, C)
    print("#" + str(test_case), ans + 1)