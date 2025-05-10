import math
import sys

sys.stdin = open("boj.txt", "r")
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

# 슬라임 에너지는 2의 자연수 2 <= K <= 1000000

# K = A * B
K = int(input())
# 분할할때마다 흠집 + 1
# 흠집이 T개인 슬라임 분할하면 흠집 T + 1

# 에라토스테네스의 체를 사용해서 소수 배열 만들것.
prime = [False] * 1000001
for i in range(2, 1001):
    if prime[i]: continue
    for j in range(i * i, 1000001, i):
        prime[j] = True


def dfs(N):
    # 소수까지 도착했다면
    if N < 2 or not prime[N]:
        return 0
    min_value = 10 ** 9
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            # 소수와 소수로 나뉘어진 값으로 나누기
            depth = 1 + max(dfs(i), dfs(N // i))
            min_value = min(min_value, depth)
    return min_value


print(dfs(K))