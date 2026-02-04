# 프로그래머스 양궁대회회

def solution(n, info):
    def gap(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == 0 and info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def better(a, b):
        for i in range(10, -1, -1):
            if a[i] != b[i]:
                return a[i] > b[i]
        return False

    best = None
    best_gap = 0

    def dfs(idx, left, ryan):
        nonlocal best, best_gap

        if idx == -1:
            ryan[10] += left
            g = gap(ryan)
            if g > 0 and (g > best_gap or (g == best_gap and (best is None or better(ryan, best)))):
                best_gap = g
                best = ryan[:]
            ryan[10] -= left
            return

        need = info[idx] + 1
        if left >= need:
            ryan[idx] = need
            dfs(idx - 1, left - need, ryan)
            ryan[idx] = 0

        dfs(idx - 1, left, ryan)

    dfs(10, n, [0] * 11)
    return best if best is not None else [-1]
