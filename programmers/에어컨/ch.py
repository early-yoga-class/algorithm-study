def solution(temperature, t1, t2, a, b, onboard):

    # dp[온도] = 현재 시간에 그 온도가 되는 최소 비용
    dp = {temperature: 0}

    if temperature > t2:
        aircon_dir = -1
    else:
        aircon_dir = 1

    def off_next_temp(cur_temp):
        if cur_temp < temperature:
            return cur_temp + 1
        elif cur_temp > temperature:
            return cur_temp - 1
        return cur_temp

    def is_valid(time, temp):
        if onboard[time] == 1:
            return t1 <= temp <= t2
        return True

    for time in range(len(onboard) - 1):
        next_dp = {}

        for cur_temp, cur_cost in dp.items():
            # 후보 온도 저장
            candidates = []

            # 에어컨 끄기
            candidates.append((off_next_temp(cur_temp), 0))
            # 에어컨 켜기 a
            candidates.append((cur_temp + aircon_dir, a))
            # 에어컨 켜기 b
            candidates.append((cur_temp, b))

            for next_temp, cost in candidates:
                if not is_valid(time + 1, next_temp): continue

                next_cost = cur_cost + cost

                if next_temp not in next_dp:
                    next_dp[next_temp] = next_cost
                else:
                    next_dp[next_temp] = min(next_dp[next_temp], next_cost)

        # 다음 time
        dp = next_dp

    return min(dp.values())