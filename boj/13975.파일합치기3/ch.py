import heapq
import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    ans = 0
    K = int(input())
    pq = [int(_) for _ in input().split()]
    heapq.heapify(pq)
    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        heapq.heappush(pq, a + b)
        ans += a + b

    print(ans)