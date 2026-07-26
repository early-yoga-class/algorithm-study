import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]

    gate_set = set(gates)
    summit_set = set(summits)

    def dijkstra(start, cost):
        cost[start] = 0
        heap = [(0, start)]

        while heap:
            current_intensity, current_node = heapq.heappop(heap)

            if current_intensity > cost[current_node]:
                continue

            # 산봉우리에 도착하면 더 이동하지 않음
            if current_node in summit_set:
                continue

            for next_node, edge_cost in graph[current_node]:
                # 다른 출입구를 중간에 지나가지 않음
                if next_node in gate_set:
                    continue

                new_intensity = max(current_intensity, edge_cost)

                if new_intensity >= cost[next_node]:
                    continue

                cost[next_node] = new_intensity
                heapq.heappush(heap, (new_intensity, next_node))

    for node_a, node_b, edge_cost in paths:
        graph[node_a].append((node_b, edge_cost))
        graph[node_b].append((node_a, edge_cost))

    min_summit = float('inf')
    min_intensity = float('inf')

    for gate in gates:
        cost = [float('inf')] * (n + 1)
        dijkstra(gate, cost)

        for summit in summits:
            if cost[summit] < min_intensity:
                min_summit = summit
                min_intensity = cost[summit]

            elif (
                cost[summit] == min_intensity
                and summit < min_summit
            ):
                min_summit = summit

    return [min_summit, min_intensity]