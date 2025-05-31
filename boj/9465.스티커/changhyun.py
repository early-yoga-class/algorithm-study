T = int(input())

for t in range(T):
    n = int(input())
    dp = [[0] * n for _ in range(2)]
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]

    for j in range(2, n):
        dp[0][j] = max(dp[1][j - 2], dp[1][j - 1]) + stickers[0][j]
        dp[1][j] = max(dp[0][j - 2], dp[0][j - 1]) + stickers[1][j]

    print(max(dp[0][n - 1], dp[1][n - 1]))