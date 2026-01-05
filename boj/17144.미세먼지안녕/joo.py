import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
 
cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    # 확산량 = 해당 칸의 미세먼지 / 5 (정수 나눗셈)
    # 남은 양 = 원래 양 - (확산량 × 확산된 방향 수)
    temp = [[0] * C for _ in range(R)]
    
    for x in range(R):
        for y in range(C):
            if room[x][y] > 0:
                spread_amount = room[x][y] // 5
                spread_count = 0
                
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        temp[nx][ny] += spread_amount
                        spread_count += 1
                
                temp[x][y] += room[x][y] - (spread_amount * spread_count)
            elif room[x][y] == -1:
                temp[x][y] = -1
    
    return temp

def clean():
    # 원래있던 값들을 살리기 위해 가장 마지막 순서부터 처리
    top, bottom = cleaner[0], cleaner[1]
    
    # 위쪽

    for i in range(top - 1, 0, -1):
        room[i][0] = room[i-1][0]

    for j in range(0, C - 1):
        room[0][j] = room[0][j+1]

    for i in range(0, top):
        room[i][C-1] = room[i+1][C-1]

    for j in range(C - 1, 1, -1):
        room[top][j] = room[top][j-1]
        
    room[top][1] = 0  
    
    # 아래쪽

    for i in range(bottom + 1, R - 1):
        room[i][0] = room[i+1][0]

    for j in range(0, C - 1):
        room[R-1][j] = room[R-1][j+1]

    for i in range(R - 1, bottom, -1):
        room[i][C-1] = room[i-1][C-1]

    for j in range(C - 1, 1, -1):
        room[bottom][j] = room[bottom][j-1]
        
    room[bottom][1] = 0 

# T초 동안 시뮬레이션
for _ in range(T):
    room = spread()
    clean()

print(sum(sum(row) for row in room) + 2)