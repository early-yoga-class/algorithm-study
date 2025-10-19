import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)
jobs = [0] * (N + 1)
time = [0] * (N + 1)
for i in range(1, N + 1):
    context = list(map(int, input().split()))
    time[i] = context[0]
    for j in context[2:]:
        graph[j].append(i)
    jobs[i] = context[1]

dp = [0] * (N + 1)
q = deque()

for i in range(1, N + 1):
    if jobs[i] == 0:
        dp[i] = time[i]
        q.append(i)

while q:
    current = q.popleft()
    for neighbor in graph[current]:
        dp[neighbor] = max(dp[neighbor], dp[current] + time[neighbor])
        jobs[neighbor] -= 1
        if jobs[neighbor] == 0:
            q.append(neighbor)

print(max(dp))