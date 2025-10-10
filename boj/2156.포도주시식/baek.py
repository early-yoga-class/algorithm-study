# 백준 2156번 포도주 시식

n = int(input())
drink = []
for i in range(n):
    drink.append(int(input()))    
dp = [0] * n

if n == 1:
    print(drink[0])
elif n == 2:
    print(drink[0] + drink[1])
elif n == 3:
    print(max(drink[0] + drink[1], drink[0] + drink[2], drink[1] + drink[2]))
else:
    dp[0] = drink[0]
    dp[1] = drink[0] + drink[1]
    dp[2] = max(dp[1], drink[0] + drink[2], drink[1] + drink[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2]+drink[i], dp[i-3]+drink[i-1]+drink[i])
    print(dp[-1])