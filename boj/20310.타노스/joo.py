import sys

s = sys.stdin.readline().strip()

count_zero = 0
count_one = 0

result = []

for si in s:

    if si == '0':
        count_zero += 1
    else:
        count_one += 1

rem_zero = count_zero // 2
rem_one = count_one // 2

seen_zero = 0

for si in s:
    if si == '1' and rem_one > 0:
        rem_one -= 1
        continue

    if si == '0' and rem_zero > 0:
        seen_zero += 1
        if (count_zero - seen_zero) >= rem_zero:
            result.append(si)
            continue
        rem_zero -= 1
        continue

    result.append(si)

print(''.join(result))


