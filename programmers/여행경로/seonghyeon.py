from collections import defaultdict
from copy import deepcopy

def solution(tickets):
    graph = defaultdict(list)
    for depart, dest in tickets:
        graph[depart].append(dest)

    for key in graph:
        graph[key].sort(reverse=True)

    count = len(tickets)
    answer = []

    def dfs(curr, route, graph):
        if len(route) ==count + 1:
            return route

        if not graph[curr]:
            return None

        for i in range(len(graph[curr]) - 1, -1, -1):
            next_graph = deepcopy(graph)
            dest = next_graph[curr].pop(i)

            new_route = dfs(dest, route + [dest], next_graph)
            if new_route:
                return new_route

        return None

    return dfs("ICN", ["ICN"], graph)