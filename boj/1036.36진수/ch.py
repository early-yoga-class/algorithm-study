import sys

N = int(input())
nums = [input().strip() for _ in range(N)]
K = int(input())

def char_to_int(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    return ord(c) - ord('A') + 10

def int_to_char(v):
    if v < 10:
        return chr(v + ord('0'))
    return chr(v - 10 + ord('A'))

# 36진수를 10진수로 변환
def conver_36_to_10(string):
    ret = 0
    L = len(string)
    for i, c in enumerate(string):
        ret += char_to_int(c) * (36 ** (L - 1 - i))
    return ret

# 10진수를 36진수로 변환
def conver_10_to_36(x):
    if x == 0:
        return "0"
    out = []
    while x > 0:
        x, r = divmod(x, 36)
        out.append(int_to_char(r))
    return ''.join(reversed(out))

# 해당 5개를 찾아 Z로 변환
def calculate(comb, target):
    if not comb:
        return conver_36_to_10(target)

    temp = []
    for c in target:
        temp.append('Z' if c in comb else c)

    return conver_36_to_10(''.join(temp))

# 각 문자를 Z로 바꿨을때 총 합의 증가 계산
z_total = [0] * 36
for s in nums:
    p = 0
    for c in reversed(s):
        v = char_to_int(c)
        z_total[v] += (35 - v) * (36 ** p) # 현재 자리수의 값을 z로 변경한 후의 값
        p += 1

# Z로 바꿨을 때 총합중 큰 순으로 정렬
order = sorted(range(36), key=lambda v: z_total[v], reverse=True)
# 큰 순서로 K개만큼 해당 뽑기
picked = order[:min(K, 36)]
# set으로 중복 제거
comb = set(int_to_char(v) for v in picked)

answer = 0
for s in nums:
    answer += calculate(comb, s)
print(conver_10_to_36(answer))