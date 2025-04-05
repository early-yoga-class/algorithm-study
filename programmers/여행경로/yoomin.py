def solution(tickets):
    tickets.sort()
    result = ["ICN"]
    visited = [False]*len(tickets)
    def dfs(n):
        key = result[-1]
        if n == len(tickets)-1:
            return result
        for i,val in enumerate(tickets):
            start = val[0] 
            end = val[1] 
            if not visited[i] and start == key:
                visited[i] = True
                result.append(end)
                dfs(n+1)
                visited[i] = False
                result.pop()
    answer = dfs(0)
    return answer