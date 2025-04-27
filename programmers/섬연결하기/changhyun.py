import heapq
def solution(n, costs):
    answer = 0    
    parent = [i for i in range(n)]
    
    pq = []
    for u, v, cost in costs:
        heapq.heappush(pq, (cost, u, v))

    def find(a):
        if a == parent[a]:
            return a
        else:
            parent[a] = find(parent[a])
            return parent[a]
            
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[b] = a

    result = 0
    useEdges = 0
    while useEdges < n - 1:
        w, s, e = heapq.heappop(pq)
        if find(s) != find(e):
            union(s, e)
            result += w
            useEdges += 1

    return result