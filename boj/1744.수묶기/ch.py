import sys

N = int(input())

p_arr = []
n_arr = []
zero_cnt = 0
one_cnt = 0

answer = 0
for i in range(N):
    num = int(input())

    if num == 0: zero_cnt += 1
    elif num == 1: one_cnt += 1
    elif num > 1:
        p_arr.append(num)
    else:
        n_arr.append(num)

n_arr.sort()
p_arr.sort(reverse=True)

for i in range(0, len(n_arr) - 1, 2):
    answer += n_arr[i] * n_arr[i + 1]

if len(n_arr) % 2 == 1:
    if zero_cnt == 0:
        answer += n_arr[-1]

for i in range(0, len(p_arr) - 1, 2):
    answer += p_arr[i] * p_arr[i + 1]

if len(p_arr) % 2 == 1:
    answer += p_arr[-1]
    
answer += one_cnt

print(answer)