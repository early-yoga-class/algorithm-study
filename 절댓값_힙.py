import sys
import heapq

n = int(sys.stdin.readline().strip())

arr = []

for _ in range(n):
    num = int(sys.stdin.readline().strip()) 
    if (num):
        heapq.heappush(arr,(abs(num),num))
    else:
        if (arr):
            print(arr[0][1])
            heapq.heappop(arr)
        else:
            print(0)
        
