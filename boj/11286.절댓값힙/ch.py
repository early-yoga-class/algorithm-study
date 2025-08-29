import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

heap = []
numbers = defaultdict(list)
N = int(input())

while N > 0:
    num = int(input())

    if num != 0:
        heapq.heappush(heap, abs(num))
        heapq.heappush(numbers[abs(num)], num)
    else:
        if len(heap) <= 0: print(0)
        else:
            print(heapq.heappop(numbers[heapq.heappop(heap)]))
    N -= 1