import sys
from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)
ans = 0

prime_num = [False] * (N + 1)

#에라토스테네스의 체
for i in range(2, int(N**0.5) + 1):
    if prime_num[i]: continue

    for j in range(i * i, N + 1 , i):
        prime_num[j] = True

# 그래프 그리기
for i, el in enumerate(map(int, input().split())):
    graph[el].append(i + 2)

# BFS
q = deque([1])
dist = [0] * (N + 1)
dist[1] = 1

while q:
    current = q.popleft()

    for neighbor in graph[current]:
        if dist[neighbor] != 0: continue
        dist[neighbor] = dist[current] + 1
        q.append(neighbor)

# 레벨별 카운트
level_count = [0] * (N + 1)
for d in dist[1:]:
    level_count[d - 1] += 1

# 소수 레벨에서 최댓값 찾기
ans = 0
for i in range(2, N):
    if not prime_num[i]:
        sum = 0
        for j in range(i, N, i):
            sum += level_count[j]
            if sum > ans:
                ans = sum

print(ans + 1)