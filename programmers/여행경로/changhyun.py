from collections import defaultdict, deque

def solution(tickets):
    answer = []
    graph = defaultdict(list)

    n = len(tickets)
    for ticket_idx, (start, end) in enumerate(tickets):
        graph[start].append((end, ticket_idx))

    for city in graph:
        graph[city].sort()

    queue = deque()
    queue.append(("ICN", ["ICN"], [False] * n))

    while queue:
        current, visited, used_ticket = queue.popleft()
        if len(visited) == n + 1:
            answer = visited
            break
        for dest, ticket_idx in graph[current]:
            if not used_ticket[ticket_idx]:
                new_used = list(used_ticket)
                new_used[ticket_idx] = True
                queue.append((dest, visited + [dest], new_used))

    return answer