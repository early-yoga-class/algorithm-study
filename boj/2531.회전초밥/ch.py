import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

count = [0] * (d + 1)

unique_cnt = 0
for i in range(k):
    if count[sushi[i]] == 0:
        unique_cnt += 1
    count[sushi[i]] += 1


if count[c] == 0:
    answer = unique_cnt + 1
else:
    answer = unique_cnt

start = 0
for end in range(k, k + N - 1):
    left_sushi = sushi[start % N]
    count[left_sushi] -= 1
    if count[left_sushi] == 0:
        unique_cnt -= 1

    right_sushi = sushi[end % N]
    if count[right_sushi] == 0:
        unique_cnt += 1
    count[right_sushi] += 1

    start += 1

    if count[c] == 0:
        current = unique_cnt + 1
    else:
        current = unique_cnt

    if current > answer:
        answer = current

print(answer)