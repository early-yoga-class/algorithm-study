T = int(input())

for test_case in range(1, T + 1):
    cross_dx = [-1, 1, 0, 0]
    cross_dy = [0, 0, -1, 1]

    diagonal_dx = [-1, -1, 1, 1]
    diagonal_dy = [-1, 1, -1, 1]

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0

    for x in range(N):
        for y in range(N):
            cross_sum = board[x][y]
            for d in range(4):
                for step in range(1, M):
                    nx = x + cross_dx[d] * step
                    ny = y + cross_dy[d] * step
                    if 0 <= nx < N and 0 <= ny < N:
                        cross_sum += board[nx][ny]

            diagonal_sum = board[x][y]
            for d in range(4):
                for step in range(1, M):
                    nx = x + diagonal_dx[d] * step
                    ny = y + diagonal_dy[d] * step
                    if 0 <= nx < N and 0 <= ny < N:
                        diagonal_sum += board[nx][ny]

            max_flies = max(max_flies, cross_sum, diagonal_sum)

    print(f"#{test_case} {max_flies}")