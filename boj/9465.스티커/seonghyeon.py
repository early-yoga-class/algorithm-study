t = int(input())

for _ in range(t):
    n = int(input())

    sticker = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1], max(dp[0][i-2],dp[1][i-2])) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], max(dp[0][i-2], dp[1][i-2])) + sticker[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))


