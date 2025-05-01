import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, p = map(int, input().split())

A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    cost = B[node] - A[node]
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            cost += dfs(neighbor)

    if cost < 0: cost = 0

    return cost

visited[p] = 1
print(dfs(p))