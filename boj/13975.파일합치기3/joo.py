import sys
import heapq

input = sys.stdin.readline


t = int(input()) 

for _ in range(t):
    k = int(input())  
    files = list(map(int, input().split())) 
    
    
    heapq.heapify(files)
    total_cost = 0
    
    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(files, cost)
        
    print(total_cost)

