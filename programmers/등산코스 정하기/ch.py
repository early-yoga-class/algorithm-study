from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    INF = float('inf')

    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    intensity = [INF] * (n + 1)
    gate_set = set(gates)
    summit_set = set(summits)
    heap = []
    
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(heap, (0, gate))
    
    while heap:
        curr_intensity, curr_node = heapq.heappop(heap)
        
        # 현재까지 도착한 노드가 최솟값 갱신이 아니면 멈춤
        if curr_intensity > intensity[curr_node]: continue
        # 현재 노드가 산봉우리면 탐색 멈춤
        if curr_node in summit_set: continue
        
        for neighbor, weight in graph[curr_node]:
            # 다음 이동할 노드가 출입구면 멈춤
            if neighbor in gate_set: continue
            
            new_intensity = max(weight, curr_intensity)
            
            if new_intensity < intensity[neighbor]:
                intensity[neighbor] = new_intensity
                heapq.heappush(heap, (new_intensity, neighbor))
            
    answer = [0, INF]
    for summit in sorted(summits):
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
            
    return answer