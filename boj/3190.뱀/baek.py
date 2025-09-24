# 백준 3190번 뱀

from collections import deque

N = int(input())
load = [[0]*N for i in range(N)]

K = int(input())
for i in range(K):
    x, y = map(int, input().split())
    load[x-1][y-1] = 1

# 행, 열 기준 오->아->왼->위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

change_list = []
Z = int(input())
for i in range(Z):
    a, b = input().split()
    a = int(a)
    change_list.append((a, b))
dir_check = 0

def change_dir(instruction):
    global dir
    if instruction == "D":
        dir += 1
        dir %= 4
    if instruction == "L":
        dir -= 1
        dir %= 4

snake = deque()
snake.append((0, 0))
time = 0

while True:
    time += 1
        
    x, y = (snake[0][0] + dx[dir]), (snake[0][1] + dy[dir])
    
    if not (0 <= x < N and 0 <= y < N):
        break
    
    if (x, y) in snake:
        break
    
    snake.appendleft((x, y))
    
    if load[x][y] == 1:
        load[x][y] = 0
    else:
        snake.pop()
    
    if change_list[dir_check][0] == time:
        change_dir(change_list[dir_check][1])
        if dir_check < Z-1:
            dir_check += 1

print(time)