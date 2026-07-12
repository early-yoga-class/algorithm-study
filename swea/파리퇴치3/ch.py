T = int(input())

p_directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

x_directions = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    answer = 0

    for x in range(N):
        for y in range(N):
            p_sum = board[x][y]
            x_sum = board[x][y]

            for dx, dy in p_directions:
                for distance in range(1, M):
                    nx = x + dx * distance
                    ny = y + dy * distance

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        break

                    p_sum += board[nx][ny]

            for dx, dy in x_directions:
                for distance in range(1, M):
                    nx = x + dx * distance
                    ny = y + dy * distance

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        break

                    x_sum += board[nx][ny]

            answer = max(answer, p_sum, x_sum)

    print(f"#{tc} {answer}")