def solution(tickets):
    n = len(tickets)
    answer = []
    
    def dfs(curr, path, used):
        if len(path) == n + 1:
            answer.append(path)
            return
        for i in range(n):
            if not used[i] and tickets[i][0] == curr:
                used[i] = True
                dfs(tickets[i][1], path + [tickets[i][1]], used)
                used[i] = False 

    used = [False] * n
    dfs("ICN", ["ICN"], used)
    
    answer.sort()
    return answer[0]
