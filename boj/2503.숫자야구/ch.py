n = int(input())
hints = []

for _ in range(n):
    num, s, b = input().split()
    num_arr = [int(d) for d in num]
    hints.append((num_arr, int(s), int(b)))

count = 0

# strike, ball 같은지 체크하는 함수
def check(candidate, target, hint_strike, hint_ball):
    strike = 0
    ball = 0
    for i in range(3):
        if candidate[i] == target[i]:
            strike += 1
        elif candidate[i] in target:
            ball += 1
    return strike == hint_strike and ball == hint_ball


for number in range(123, 988):  # 987까지
    hundred = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    if hundred == 0 or tens == 0 or ones == 0:
        continue
    if hundred == tens or tens == ones or hundred == ones:
        continue

    candidate = [hundred, tens, ones]
    flag = True

    for target, hint_s, hint_b in hints:
        if not check(candidate, target, hint_s, hint_b):
            flag = False
            break

    if flag:
        count += 1

print(count)