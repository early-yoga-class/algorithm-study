def solution(temperature, t1, t2, a, b, onboard):
    answer = 0

    INF = int(1e9)
    OFFSET = 10
    MIN_TEMP = -10
    MAX_TEMP = 40

    outdoor_temp = temperature

    DP = [[INF] * 51 for _ in range(len(onboard))]
    DP[0][temperature + OFFSET] = 0

    def judge_good_temp(indoor_temp):
        return t1 <= indoor_temp <= t2

    def air_conditioner_dead(indoor_temp):
        if indoor_temp < outdoor_temp:
            return indoor_temp + 1
        elif indoor_temp > outdoor_temp:
            return indoor_temp - 1
        else:
            return indoor_temp

    def air_conditioner_run(indoor_temp):
        return [
            (indoor_temp - 1, a),
            (indoor_temp + 1, a),
            (indoor_temp, b),
        ]

    for time in range(len(onboard) - 1):
        for indoor_temp in range(MIN_TEMP, MAX_TEMP + 1):
            cur_cost = DP[time][indoor_temp + OFFSET]

            if cur_cost == INF:
                continue

            # 1. 에어컨 OFF
            next_temp = air_conditioner_dead(indoor_temp)

            if MIN_TEMP <= next_temp <= MAX_TEMP:
                if onboard[time + 1] == 0 or judge_good_temp(next_temp):
                    DP[time + 1][next_temp + OFFSET] = min(
                        DP[time + 1][next_temp + OFFSET],
                        cur_cost,
                    )

            # 2. 에어컨 ON
            for next_temp, cost in air_conditioner_run(indoor_temp):
                if MIN_TEMP <= next_temp <= MAX_TEMP:
                    if onboard[time + 1] == 0 or judge_good_temp(next_temp):
                        DP[time + 1][next_temp + OFFSET] = min(
                            DP[time + 1][next_temp + OFFSET],
                            cur_cost + cost,
                        )

    answer = min(DP[len(onboard) - 1])

    return answer
