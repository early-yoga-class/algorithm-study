# 백준 1504번 특정한 최단 경로

import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

INF = float('inf')

def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, now = heapq.heappop(pq)

        if dist[now] < cost:
            continue

        for nxt, weight in graph[now]:
            new_cost = cost + weight

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return dist

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

answer = min(path1, path2)

if answer == INF:
    print(-1)
else:
    print(answer)