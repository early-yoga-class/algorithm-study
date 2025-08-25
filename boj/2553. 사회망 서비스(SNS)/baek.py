# 백준 2533 사회망 서비스(SNS)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
graph = [[] for _ in range(n+1)]

# 양방향 트리 연결
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dp[node][0] : node가 얼리어답터가 아닐 때, node를 포함한 서브트리의 최소 얼리어답터 수
# dp[node][1] : node가 얼리어답터일 때, node를 포함한 서브트리의 최소 얼리어답터 수
dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
            dp[node][0] += dp[next][1] # node가 얼리어답터가 아니면 자식은 반드시 얼리어답터
            dp[node][1] += min(dp[next][0], dp[next][1]) # node가 얼리어답터라면 자식 상관없음음
            
dfs(1)
print(min(dp[1][0], dp[1][1])) 