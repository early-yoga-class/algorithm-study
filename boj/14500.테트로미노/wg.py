import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0
visited = [[False] * M for _ in range(N)]


def DFS(x, y):
    global answer

    def dfs(nx, ny, depth, total):
        global answer

        if depth == 4:
            answer = max(answer, total)
            return

        for d in range(4):
            px = nx + dx[d]
            py = ny + dy[d]
            if 0 <= px < N and 0 <= py < M and not visited[px][py]:
                visited[px][py] = True
                dfs(px, py, depth + 1, total + board[px][py])
                visited[px][py] = False

    visited[x][y] = True
    dfs(x, y, 1, board[x][y])
    visited[x][y] = False


#  ㅗ, ㅜ, ㅏ, ㅓ 모양 별도 처리
def fuck_u_shape(x, y):
    global answer

    center = board[x][y]

    fuck_u_shapes = [
        [(0,1), (0,-1), (-1,0)], # ㅗ
        [(0,1), (0,-1), (1,0)],  # ㅜ
        [(-1,0), (1,0), (0,1)],  # ㅏ
        [(-1,0), (1,0), (0,-1)]  # ㅓ
    ]

    for shape in fuck_u_shapes:
        total = center
        valid = True

        for dx_, dy_ in shape:
            nx = x + dx_
            ny = y + dy_
            if 0 <= nx < N and 0 <= ny < M:
                total += board[nx][ny]
            else:
                valid = False
                break

        if valid:
            answer = max(answer, total)


for i in range(N):
    for j in range(M):
        DFS(i, j)
        fuck_u_shape(i, j)

print(answer)
