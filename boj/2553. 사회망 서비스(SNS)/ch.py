import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
graph = defaultdict(list)

N = int(input())

for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)

def dfs(current):
    visited[current] = True
    dp[current][1] = 1

    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor)
            # 현재 노드가 얼리어답터가 아니면, 자식은 반드시 얼리어답터
            dp[current][0] += dp[neighbor][1]
            # 현재 노드가 얼리어답터이면, 자식은 맞거나 틀리거나
            dp[current][1] += min(dp[neighbor][0], dp[neighbor][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))