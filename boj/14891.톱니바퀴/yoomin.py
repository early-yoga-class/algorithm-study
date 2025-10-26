import sys
from collections import deque
import copy

wheel = [False]
for _ in range(4):
    wheel.append(deque(map(int,sys.stdin.readline().strip())))

N = int(input())

def dfs(num,dir,now):
    global dp
    dp[num] = dir
    if dir == 1:
        new_dir = -1
    else:
        new_dir = 1

    if now == 'l':
        left = num - 1
        if 1 <= left <= 4:
            if not wheel[left][2] == wheel[num][6]:
                dfs(left,new_dir,'l')
    
    else:
        right = num + 1
        if 1 <= right <= 4:
            if not wheel[right][6] == wheel[num][2]:
                dfs(right,new_dir,'r')
    

for _ in range(N):
    dp = [0]*5
    wheel_num, dir = map(int,sys.stdin.readline().split())
    left = wheel_num - 1
    right = wheel_num + 1
    
    if dir == 1:
        new_dir = -1
    else:
        new_dir = 1
        
    if 1 <= left <= 4:
        if not wheel[left][2] == wheel[wheel_num][6]:
            dfs(left,new_dir,'l')
    
    if 1 <= right <= 4:
        if not wheel[right][6] == wheel[wheel_num][2]:
            dfs(right,new_dir,'r')

    dp[wheel_num] = dir

    for i in range(1,5):
        if dp[i] == 1:
            n_s = wheel[i].pop()
            wheel[i].appendleft(n_s)
        elif dp[i] == -1:
            n_s = wheel[i].popleft()
            wheel[i].append(n_s)


sum = 0

for i in range(1,5):
    if wheel[i][0]:
        sum += 2**(i-1)

print(sum)
