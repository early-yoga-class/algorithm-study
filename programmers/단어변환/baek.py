def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    n = len(words)
    used = [False] * n
    answer = []
    
    def possible(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1
    
    def dfs(now, target, cnt, used):
        
        if now == target:
            answer.append(cnt)
            return
        elif sum(used) == len(words):
            return
        
        for i in range(n):
            if not used[i] and possible(now, words[i]):
                used[i] = True
                dfs(words[i], target, cnt + 1, used)
                used[i] = False
                
    dfs(begin, target, 0, used)

    return min(answer) if answer else 0