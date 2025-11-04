from collections import deque

gears = []
for _ in range(4):
    gears.append(deque(map(int, list(input().strip()))))

K = int(input())

def rotate(gear_num, direction):
    # 시계방향
    if direction == 1:
        gears[gear_num].appendleft(gears[gear_num].pop())
    else:  # 반시계 방향
        gears[gear_num].append(gears[gear_num].popleft())

def check_and_rotate(gear_num, direction):

    directions = [0] * 4
    directions[gear_num] = direction
    

    for i in range(gear_num, 0, -1):
        if gears[i][6] != gears[i-1][2]: 
            directions[i-1] = -directions[i]
        else:
            break

    for i in range(gear_num, 3):
        if gears[i][2] != gears[i+1][6]: 
            directions[i+1] = -directions[i]
        else:
            break

    for i in range(4):
        if directions[i] != 0:
            rotate(i, directions[i])

for _ in range(K):
    gear_num, direction = map(int, input().split())
    check_and_rotate(gear_num - 1, direction) 

score = 0
for i in range(4):
    if gears[i][0] == 1:  
        score += 2 ** i

print(score)