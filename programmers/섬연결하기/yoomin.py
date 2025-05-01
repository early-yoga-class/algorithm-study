import heapq

def solution(n, costs):
    visited = [False] * n
    graph = [[] for _ in range(n)]
    for a, b, cost in costs:
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    island = []
    visited[0] = True

    #이웃을 다 큐에 넣는다.
    for neighbor in graph[0]:
        heapq.heappush(island, neighbor)

    total = 0
    
    while island:
        cost, node = heapq.heappop(island)
        if visited[node]:
            continue
        visited[node] = True
        total += cost
        for neighbor in graph[node]:
            heapq.heappush(island, neighbor)

    return total
