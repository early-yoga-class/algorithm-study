import sys
from collections import defaultdict
from collections import deque
N = int(input())

graph = [[] for _ in range(N+1)]
time = [0]*(N+1)
result = [0]*(N+1)
indegree = defaultdict(int)

for n in range(1,N+1):
    lst = list(map(int,sys.stdin.readline().split()))
    for i,l in enumerate(lst):
        if l == -1:
            continue
        if i == 0:
            time[n] = l
        else:
            graph[l].append(n)
            indegree[n] += 1

queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)
        result[i] = time[i]

while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
        result[neighbor] = max(result[neighbor],time[neighbor]+result[current])


for i in result:
    if i == 0:
        continue
    print(i)