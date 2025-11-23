import math
import sys
N = int(input())

prime_checked = [False] * (N + 1)
prime_checked[0] = prime_checked[1] = True
for i in range(2, int(math.sqrt(N)) + 1):
    if prime_checked[i]: continue
    for j in range(i * i, (N + 1), i):
        prime_checked[j] = True

prime_numbers = [i for i, val in enumerate(prime_checked) if prime_checked[i] == False]
answer = 0
left = 0
right = 0
total = 0
while True:
    # N보다 작으면 오른쪽 길이를 늘린다.
    if total < N:
        # 끝에 도착하면 멈춘다.
        if right == len(prime_numbers): break
        total += prime_numbers[right]
        right += 1
    else:
        # 가능한 경우
        if total == N: answer += 1
        total -= prime_numbers[left]
        left +=1

print(answer)