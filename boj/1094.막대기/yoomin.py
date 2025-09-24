import sys 
import heapq
X = int(input())
sticks = [64]
heapq.heapify(sticks)
total = 64

while True:
    if X == 64:
        print(1)
        break
    min_stick = heapq.heappop(sticks)
    half = min_stick//2
    total -= min_stick
    
    if (half + total) >= X:
        heapq.heappush(sticks,half)
        total +=half
    else:
        heapq.heappush(sticks,half)
        heapq.heappush(sticks,half)
        total += half*2


    if total == X:
        print(len(sticks))
        break
