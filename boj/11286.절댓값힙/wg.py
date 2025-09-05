import sys
import heapq 

N = int(sys.stdin.readline().strip())
array = []
for i in range(N):
  x = int(sys.stdin.readline().strip())
  if x != 0:
    heapq.heappush(array, [abs(x), x])
  else:
    if len(array) == 0:
      print(0)
    else:
      print(heapq.heappop(array)[1])