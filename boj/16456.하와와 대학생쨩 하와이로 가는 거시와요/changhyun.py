import sys

input = sys.stdin.readline

# 바로 다음 섬으로 이동 +1

# 한 섬을 건너뛰고 다음 섬으로 이동 + 2

# 이전 섬으로 이동 -1

# 1 <= N <= 50000
N = int(input())
dp = [0] * 50001
if N == 1:
    print(1)
    exit(0)

dp[2] = 1
dp[3] = 2
dp[4] = 3
for i in range(5, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 3]) % 1000000009

print(dp[N])