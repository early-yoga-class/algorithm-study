# 백준 17144번 미세먼지안녕

def 먼지_확산(r, c, room):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    store = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                store[i][j] = -1
                continue

            if room[i][j] > 0:
                cnt = 0
                temp = room[i][j] // 5

                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                        store[ni][nj] += temp
                        cnt += 1

                store[i][j] += room[i][j] - temp * cnt

    return store


def 순환_경로_만들기(r, c, top, bottom):

    up_path = []
    down_path = []

    for y in range(1, c):
        up_path.append((top, y))
    for x in range(top - 1, -1, -1):
        up_path.append((x, c - 1))
    for y in range(c - 2, -1, -1):
        up_path.append((0, y))
    for x in range(1, top + 1): 
        up_path.append((x, 0))

    for y in range(1, c):
        down_path.append((bottom, y))
    for x in range(bottom + 1, r): 
        down_path.append((x, c - 1))
    for y in range(c - 2, -1, -1): 
        down_path.append((r - 1, y))
    for x in range(r - 2, bottom - 1, -1):
        down_path.append((x, 0))

    return up_path, down_path


def 먼지_이동(cleaner, room, up_path, down_path):
    top, bottom = cleaner

    prev = 0
    for x, y in up_path:
        room[x][y], prev = prev, room[x][y]

    prev = 0
    for x, y in down_path:
        room[x][y], prev = prev, room[x][y]

    room[top][0] = -1
    room[bottom][0] = -1

    return room


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

top, bottom = cleaner
up_path, down_path = 순환_경로_만들기(R, C, top, bottom)

for _ in range(T):
    room = 먼지_확산(R, C, room)
    room = 먼지_이동(cleaner, room, up_path, down_path)

ans = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            ans += room[i][j]
print(ans)
