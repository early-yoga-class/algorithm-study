from collections import defaultdict, deque

def bfs(x, graph):
    q = deque([x])
    visited = [False] * (N + 1)
    visited[x] = True
    count = 0
    while q:
        current = q.popleft()
        for next_node in graph[current]:
            if visited[next_node]: 
                continue
            q.append(next_node)
            visited[next_node] = True
            count += 1
    return count
    

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    M = int(input())
    answer = 0
    graph = defaultdict(list)
    graph_reverse = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph_reverse[b - 1].append(a - 1)
        
    for n in range(0, N):
        if bfs(n, graph) + bfs(n, graph_reverse) == N - 1:
            answer += 1

    print(f"#{test_case} {answer}")
    