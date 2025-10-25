from collections import deque

N = int(input())

time = [0] * (N + 1) 
graph = [[] for _ in range(N + 1)]  
indegree = [0] * (N + 1) 
dp = [0] * (N + 1)  


for i in range(1, N + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  
    predecessor_count = data[1]  
    
    for j in range(2, 2 + predecessor_count):
        predecessor = data[j]  
        graph[predecessor].append(i)  
        indegree[i] += 1  

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]  

while queue:
    current = queue.popleft()
    

    for next_work in graph[current]:

        dp[next_work] = max(dp[next_work], dp[current] + time[next_work])
        
        indegree[next_work] -= 1
        
        if indegree[next_work] == 0:
            queue.append(next_work)


print(max(dp[1:N+1]))