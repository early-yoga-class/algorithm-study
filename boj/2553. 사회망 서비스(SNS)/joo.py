import sys
sys.setrecursionlimit(1500000)
input = sys.stdin.readline

def dfs(node, parent, adj):
    not_early = 0  
    early = 1      
    
    for child in adj[node]:
        if child != parent:
            child_not_early, child_early = dfs(child, node, adj)
            
    
            not_early += child_early
            
    
            early += min(child_not_early, child_early)
    
    return not_early, early

n = int(input())

if n == 1:
    print(0)
else:
    adj = [[] for _ in range(n + 1)]
    
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    
    result = dfs(1, -1, adj)
    print(min(result[0], result[1]))