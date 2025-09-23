import sys

input = sys.stdin.readline

N, K = map(int, input().split())
durs = [num for num in map(int, input().split())]
visited = [False] * N


def rotate():
    # Belt rotate
    temp = durs[-1]
    for i in range(2 * N - 1, 0, -1):
        durs[i] = durs[i - 1]
    durs[0] = temp

    # robot rotate
    for i in range(N - 1, 0, -1):
        visited[i] = visited[i - 1]
    visited[0] = False
    visited[N - 1] = False

def check_empty():
    cnt = 0
    for x in durs:
        if x == 0:
            cnt += 1
    return cnt

def robot_move():
    for i in range(N - 2, -1, -1):
        if visited[i] and not visited[i + 1] and durs[i + 1] > 0:
            visited[i] = False
            visited[i + 1] = True
            durs[i + 1] -= 1

    visited[N - 1] = False

def put_robot():
    if (not visited[0]) and durs[0] > 0:
        visited[0] = True
        durs[0] -= 1

time = 0
while check_empty() < K:
    rotate()
    robot_move()
    put_robot()
    time += 1

print(time)