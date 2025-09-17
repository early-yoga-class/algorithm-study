import sys
from collections import defaultdict

input = sys.stdin.readline


N, K = map(int, input().split())

name_lens = []

for i in range(N):
    name_lens.append(len(input().strip()))

window = defaultdict(int)

# 처음 값 넣기
window[name_lens[0]] = 1

answer = 0

# K길이만큼 움직이는 window 생성하고 이동
current = 1
prev = 0
while current < N:
    answer += window[name_lens[current]]

    window[name_lens[current]] += 1
    if current - prev >= K:
        window[name_lens[prev]] -= 1
        prev += 1

    current += 1


print(answer)