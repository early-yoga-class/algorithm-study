def find(parent, node):
    if parent[node] == node:
        return node

    parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, first, second):
    firstParent = find(parent, first)
    secondParent = find(parent, second)

    if firstParent < secondParent:
        parent[secondParent] = firstParent
    else:
        parent[firstParent] = secondParent


def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]

    costs = sorted(costs, key=lambda x: x[2])

    for start, end, value in costs:
        if find(parent, start) != find(parent, end):
            answer += value
            union(parent, start, end)

    return answer

