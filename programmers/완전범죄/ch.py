def solution(info, n, m):
    leng = len(info)
    memo = {}
    answer = float("inf")

    def dfs(thief_a, thief_b, cnt):
        nonlocal answer
        key = (cnt, thief_b)
        
        # 가지치기
        if thief_a >= n or thief_b >= m: return
        if thief_a >= answer: return    
        
        if key in memo and memo[key] <= thief_a: return
        memo[key] = thief_a
    
        if cnt == leng:
            answer = min(answer, thief_a)
            return
    
        a, b = info[cnt]
        
        if a + thief_a <= n:
            dfs(thief_a + a, thief_b, cnt + 1)

        if b + thief_b <= m:
            dfs(thief_a, thief_b + b, cnt + 1)
        
    dfs(0, 0, 0)
        
    return -1 if answer == float("inf") else answer