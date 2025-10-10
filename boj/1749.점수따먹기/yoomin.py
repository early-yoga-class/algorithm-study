import sys
from itertools import combinations

N, M = map(int,input().split())
nums = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def kadane(start,end):
    dp = [0 for _ in range(M)]
    for m in range(M):
        for n in range(start,end+1):
            dp[m] += nums[n][m]
    
    cur = dp[0]
    ans = dp[0]

    for i in dp[1:]:
        cur = max(i, i + cur)
        ans = max(cur,ans)
    
    return ans

answer = -float('inf')

for com in combinations(list(range(N)),2):
    list(com)
    ans = kadane(com[0],com[1])
    answer = max(answer,ans)

for i in range(N):
    ans = kadane(i,i)
    answer = max(answer,ans)

print(answer)