import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]

    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    gate_set = set(gates)
    summit_set = set(summits)

    INF = float('inf')
    intensity = [INF] * (n + 1)

    heap = []

    # 모든 출입구를 시작점으로
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(heap, (0, gate))

    while heap:
        current_intensity, current_node = heapq.heappop(heap)

        if current_intensity > intensity[current_node]:
            continue

        # 산봉우리에 도착하면 종료
        if current_node in summit_set:
            continue

        for next_node, edge_cost in graph[current_node]:

            # 다른 출입구는 지나가지 않음
            if next_node in gate_set:
                continue

            new_intensity = max(current_intensity, edge_cost)

            if new_intensity < intensity[next_node]:
                intensity[next_node] = new_intensity
                heapq.heappush(heap, (new_intensity, next_node))

    summits.sort()

    answer = [0, INF]

    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]

    return answer