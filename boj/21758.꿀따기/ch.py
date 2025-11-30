import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
prefix_sum = [board[0]]

for i in range(1, N):
    prefix_sum.append(prefix_sum[i - 1] + board[i])
answer = 0
# 벌 벌 통
for pos in range(1, N - 1):
    left = prefix_sum[-1] - board[0] - board[pos]
    right = prefix_sum[-1] - prefix_sum[pos]
    answer = max(answer, (left + right))

# 벌 통 벌
for pos in range(1, N - 1):
    left = prefix_sum[pos] - board[0]
    right = prefix_sum[-1] - prefix_sum[pos - 1] - board[N - 1]
    answer = max(answer, (left + right))

# 통 벌 벌
for pos in range(1, N - 1):
    left = prefix_sum[-1] - board[N - 1] - board[pos]
    right = prefix_sum[pos - 1]
    answer = max(answer, (left + right))

print(answer)