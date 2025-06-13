N, K = map(int, input().split())

result = {i:[0, 0, 0] for i in range(1, N+1)}

for j in range(N):
    num, gold, silver, bronze = map(int, input().split())
    result[num][0] += gold
    result[num][1] += silver
    result[num][2] += bronze

check = []

g, s, b = result.pop(K, None)
cnt = 1

for elem in result:
    if g < result[elem][0]:
        cnt += 1
        check.append(result[elem])

for elem in result:
    if (g == result[elem][0]) and (s < result[elem][1]):
        if result[elem] not in check:
            cnt += 1
            check.append(result[elem])

for elem in result:
    if (g == result[elem][0]) and (s == result[elem][1]) and (b < result[elem][2]):
        if result[elem] not in check:
            cnt += 1
            check.append(result[elem])

print(cnt)