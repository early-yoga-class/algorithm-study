# 백준 30414 투스타 춘배
# 유민느님의 코드를 이해해봤습니다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, P = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
soil = [0] * (N+1)  # 각 산의 최종 흙 변화량 저장
visited = [False] * (N+1) # 방문 여부 기록

graph = [[] for _ in range(N+1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur):
    soil[cur] = B[cur] - A[cur]  # 현재 산에서 필요한 흙 변화량 저장
    for child in graph[cur]:  # 연결된 산(자식) 탐색
        if visited[child]:
            continue  # 이미 방문한 산은 무시
        visited[child] = True
        dfs(child)
        if soil[child] > 0:
            soil[cur] += soil[child]  # 자식에서 남은 흙만 현재로 모아온다
            
visited[P] = True
dfs(P)
print(soil[P])