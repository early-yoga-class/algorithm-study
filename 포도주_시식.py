import sys

N = int(sys.stdin.readline().strip())

wine = []
for _ in range(N):
    wine.append(int(sys.stdin.readline().strip()))

# N이 작은 경우 예외 처리
if N == 1:
    print(wine[0])
elif N == 2:
    print(wine[0] + wine[1])
else:
    dp = [0] * N
    
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1],
                wine[0] + wine[2],
                wine[1] + wine[2])
    
    for i in range(3, N):
        dp[i] = max(dp[i-1],
                    dp[i-2] + wine[i],
                    dp[i-3] + wine[i-1] + wine[i])
    
    print(dp[N-1])