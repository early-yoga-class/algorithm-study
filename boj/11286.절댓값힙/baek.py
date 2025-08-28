# 백준 11286번  절댓값 힙

import heapq
import sys
input = sys.stdin.readline

min_heap = []
max_heap = []

for i in range(int(input())):
    n = int(input())
    if n == 0:
        if min_heap and max_heap:
            if min_heap[0] <= max_heap[0]:
                print(-heapq.heappop(min_heap))
            else:
                print(heapq.heappop(max_heap))             
        elif min_heap or max_heap:
            if min_heap:
                print(-heapq.heappop(min_heap))
            else:
                print(heapq.heappop(max_heap))
        else:
            print(0)
        
    else: 
        if n < 0:
            heapq.heappush(min_heap, -n)
        else: 
            heapq.heappush(max_heap, n)     