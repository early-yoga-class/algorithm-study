import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, P = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cost = [0] * (N+1)
soil = [0] * (N+1)
dp = []
ans = 0

def dfs(cur, parent):
    global ans
    soil[cur] = B[cur] - A[cur]  
    for child in graph[cur]:
        if child == parent:
            continue
        dfs(child, cur)
        if soil[child]>0:
            soil[cur] += soil[child]  

dfs(P,-1)
print(soil[P])
