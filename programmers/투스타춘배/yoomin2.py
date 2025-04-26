import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, P = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
soil = [0] * (N+1)
visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur):
    soil[cur] = B[cur] - A[cur] 
    for child in graph[cur]:
        if visited[child]:
            continue
        visited[child] = True
        dfs(child)
        if soil[child]>0:
            soil[cur] += soil[child]  
visited[P] = True
dfs(P)
print(soil[P])