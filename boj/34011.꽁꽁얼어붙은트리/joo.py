import sys
from collections import deque

def bfs(start,graph,N):
    visited = [False] * (N+1) # 방문 여부
    depth = [-1] * (N+1) # 루트로부터의 거리
    
    q = deque()
    q.append(start)
    visited[start] = True
    depth[start] = 0
    
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                q.append(v)
                
    return(depth)
    
    
def sieve(num):
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(num**0.5) +  1):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False
    
    primes = []
    for i in range(2,num+1):
        if is_prime[i]:
            primes.append(i)
    
    return primes
            

def solve():
    N = int(sys.stdin.readline().strip())
    
    graph = [[] for _ in range(N+1)]
    
    graph_parents = list(map(int,sys.stdin.readline().split()))
    for i in range(2,N+1):
        parents = graph_parents[i-2]
        
        graph[i].append(parents)
        graph[parents].append(i)
        
    # for j in range(1,N+1):
    #     print(f"{j}: {graph[j]}")
    
    # 깊이 구했으니, 소수인 제동거리로 갈 수 있는 노드의 수 구하기
    
    depth = bfs(1, graph, N)
    max_d = max(depth)
    
    primes_in_max_d = sieve(max_d)
    
    depth_cnt = [0] * (max_d + 1)
    
    for d in depth[1:]:
        depth_cnt[d] += 1
    
    ans = 0
    
    for prime in primes_in_max_d:
        result = 0    
        for k in range(prime, max_d+1, prime):
            result += depth_cnt[k]
        if result > ans:
            ans = result
    
    ans = max(ans,result)
            
    print(ans + 1)
    
    

solve()