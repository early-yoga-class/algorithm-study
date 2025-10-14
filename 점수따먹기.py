import sys

N, M = map(int,sys.stdin.readline().split())
val = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_sum = float('-inf')

for start_row in range(N):
    temp = [0] * M
    
    for end_row in range(start_row, N):
        for col in range(M):
            temp[col] += val[end_row][col]
        
        current_max = float('-inf')
        dp = 0
        
        for i in range(M):
            dp = max(temp[i], dp + temp[i])  
            current_max = max(current_max, dp)
        
        max_sum = max(max_sum, current_max)

print(max_sum)