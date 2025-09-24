import sys
from collections import deque
N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())


apple = deque()

for _ in range(K):
    ax, ay = list(map(int, sys.stdin.readline().split()))
    apple.append((ax,ay))
    
L = int(sys.stdin.readline().strip())

dir_ch = deque()

for _ in range(L):
    dc_time,dc_dir = list(sys.stdin.readline().split())
    dc_time = int(dc_time)
    dir_ch.append((dc_time,dc_dir))
    
    
    
    
direction = 1


snake_pos = deque()
sx, sy = (1,1)
snake_pos.append((sx,sy))

time = 0

while True:
    time +=1
    
    if direction == 1:
        sy += 1
    elif direction == 0:
        sx -= 1
    elif direction == 2:
        sx += 1
    else:
        sy -= 1
        
    if sx > N or sy > N or sx < 1 or sy < 1:
        break
    
    if (sx, sy) in snake_pos:
        break
    
    if (sx,sy) not in apple:
        snake_pos.append((sx,sy))
        snake_pos.popleft()
    else:
        snake_pos.append((sx,sy))
        apple.remove((sx,sy))

    if (time, 'L') in dir_ch or (time, 'D') in dir_ch:
        d = dir_ch.popleft()
        if d[1] == 'L':
            if direction == 0:
                direction = 3
            else:
                direction -=1
        
        if d[1] == 'D':
            if direction == 3:
                direction = 0
            else:
                direction +=1
        

print(time)