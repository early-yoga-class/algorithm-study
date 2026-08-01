def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10

    INF = 10 ** 9
    n = len(onboard)

    dp = [[INF] * 51 for _ in range(n)]
    dp[0][temperature] = 0
    
    # dp[time][temp] = time분에 실내 온도가 temp일 수 있을 때, 거기까지 드는 최소 비용

    for time in range(n - 1):
        for temp in range(51):
            if dp[time][temp] == INF:
                continue

            # 에어컨 OFF: 실외온도 방향으로 이동, 비용 0
            next_temp = temp
            if temp < temperature:
                next_temp = temp + 1
            elif temp > temperature:
                next_temp = temp - 1

            if onboard[time + 1] == 0 or t1 <= next_temp <= t2:
                dp[time + 1][next_temp] = min(
                    dp[time + 1][next_temp],
                    dp[time][temp]
                )

            # 에어컨 ON: 온도 1도 내림, 비용 a
            if temp - 1 >= 0:
                next_temp = temp - 1
                if onboard[time + 1] == 0 or t1 <= next_temp <= t2:
                    dp[time + 1][next_temp] = min(
                        dp[time + 1][next_temp],
                        dp[time][temp] + a
                    )

            # 에어컨 ON: 온도 1도 올림, 비용 a
            if temp + 1 <= 50:
                next_temp = temp + 1
                if onboard[time + 1] == 0 or t1 <= next_temp <= t2:
                    dp[time + 1][next_temp] = min(
                        dp[time + 1][next_temp],
                        dp[time][temp] + a
                    )

            # 에어컨 ON: 현재 온도 유지, 비용 b
            next_temp = temp
            if onboard[time + 1] == 0 or t1 <= next_temp <= t2:
                dp[time + 1][next_temp] = min(
                    dp[time + 1][next_temp],
                    dp[time][temp] + b
                )

    return min(dp[-1])