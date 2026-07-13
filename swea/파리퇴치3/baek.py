# swea 12712. 파리퇴치 3

def check_plus_shape(arr, n, m, x, y):
    mos = arr[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for d in range(4):
        for k in range(1, m):
            nx = x + dx[d] * k
            ny = y + dy[d] * k

            if 0 <= nx < n and 0 <= ny < n:
                mos += arr[nx][ny]

    return mos


def check_product_shape(arr, n, m, x, y):
    mos = arr[x][y]

    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    for d in range(4):
        for k in range(1, m):
            nx = x + dx[d] * k
            ny = y + dy[d] * k

            if 0 <= nx < n and 0 <= ny < n:
                mos += arr[nx][ny]

    return mos


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    answer = 0

    for i in range(N):
        for j in range(N):
            a = check_plus_shape(arr, N, M, i, j)
            b = check_product_shape(arr, N, M, i, j)
            answer = max(answer, a, b)

    print(f"#{test_case} {answer}")