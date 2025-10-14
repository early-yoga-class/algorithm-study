import sys
input = sys.stdin.readline

N = int(input())

wine_list = []
result = []

for _ in range(N):
  wine_list.append(int(input().strip()))

dp = [0] * N

dp[0] = wine_list[0]

if N > 1:
    dp[1] = wine_list[0] + wine_list[1]

if N > 2:
    dp[2] = max(wine_list[0] + wine_list[1],
                wine_list[0] + wine_list[2],
                wine_list[1] + wine_list[2])

for i in range(3, N):
  dp[i] = max(dp[i - 1], dp[i - 2] + wine_list[i], dp[i - 3] + wine_list[i - 1] + wine_list[i])

print(dp[-1])