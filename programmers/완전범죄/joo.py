def solution(info, n, m):
    INF = 10**15
    dp = [INF] * m
    dp[0] = 0  # B=0일 때 A=0

    for a_i, b_i in info:
        ndp = [INF] * m
        for b in range(m):
            if dp[b] == INF:
                continue
            # i를 A가 훔치는 경우 (B변화X, A추가)
            if dp[b] + a_i < ndp[b]:
                ndp[b] = dp[b] + a_i
            # i를 B가 훔치는 경우 (B증가, 체포선 체크)
            nb = b + b_i
            if nb < m and dp[b] < ndp[nb]:
                ndp[nb] = dp[b]
        dp = ndp

    # A < n 조건을 만족하는 최소 A
    answer = min((x for x in dp if x < n), default=INF)
    return -1 if answer == INF else answer