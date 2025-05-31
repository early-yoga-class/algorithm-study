from collections import deque

# 터널 종류 - 이동 가능 방향
def get_directions(pipe_type):
    if pipe_type == 1:
        return [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌
    elif pipe_type == 2:
        return [(-1, 0), (1, 0)]  # 상 하
    elif pipe_type == 3:
        return [(0, -1), (0, 1)]  # 좌 우
    elif pipe_type == 4:
        return [(-1, 0), (0, 1)]  # 상 우
    elif pipe_type == 5:
        return [(1, 0), (0, 1)]  # 하 우
    elif pipe_type == 6:
        return [(1, 0), (0, -1)]  # 하 좌
    elif pipe_type == 7:
        return [(-1, 0), (0, -1)]  # 상 좌
    return []

# 연결된 방향 확인
def is_connected(dr, dc, next_pipe_type):
    reverse = (-dr, -dc)
    return reverse in get_directions(next_pipe_type)

# BFS 이동 가능한 위치
def bfs(start_r, start_c, max_time):
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = 0  # 시작 위치는 0초

    while queue:
        r, c = queue.popleft()
        time_spent = visited[r][c]

        if time_spent + 1 >= max_time:
            continue

        for dr, dc in get_directions(tunnel[r][c]):
            nr, nc = r + dr, c + dc

            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc] != -1 or tunnel[nr][nc] == 0:
                continue
            if is_connected(dr, dc, tunnel[nr][nc]):
                visited[nr][nc] = time_spent + 1
                queue.append((nr, nc))

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    bfs(R, C, L)
    count = sum(1 for i in range(N) for j in range(M) if visited[i][j] != -1)
    print(f'#{tc} {count}')
