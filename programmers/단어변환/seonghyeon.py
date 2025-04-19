def solution(begin, target, words):
    global min_n
    visited = [False] * (len(words))
    result = []
    min_n = float('inf')

    def dfs(idx, n):
        global min_n
        if n == 0:
            start = idx
        else:
            start = words[idx]
        if n != 0 and words[idx] == target:
            min_n = min(min_n, n)
            return
        if n >= len(words):
            min_n = 0

        lst = []
        for i, val in enumerate(words):
            cnt = 0
            for j in range(len(val)):
                if start[j] != val[j]:
                    cnt += 1
            if cnt == 1 and not visited[i]:
                lst.append(i)
        # index를 lst에 넣는다.
        for i in lst:
            visited[i] = True
            dfs(i, n + 1)
            visited[i] = False

    dfs(begin, 0)
    return min_n