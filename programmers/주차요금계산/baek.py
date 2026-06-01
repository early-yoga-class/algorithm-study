from collections import defaultdict

def calculate_minute(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def calculate_fee(fees, car_io):
    result = []

    for key, value in car_io.items():
        if len(value) % 2 != 0:
            value.append(23 * 60 + 59)

        total_time = 0

        for i in range(0, len(value), 2):
            total_time += value[i + 1] - value[i]

        fee = fees[1]

        if total_time > fees[0]:
            extra_time = total_time - fees[0]

            if extra_time % fees[2] == 0:
                fee += (extra_time // fees[2]) * fees[3]
            else:
                fee += (extra_time // fees[2] + 1) * fees[3]

        result.append((key, fee))

    return result

def solution(fees, records):
    car_io = defaultdict(list)

    for record in records:
        time, car_num, state = record.split()
        car_io[car_num].append(calculate_minute(time))

    arr = calculate_fee(fees, car_io)
    arr.sort(key=lambda x: x[0])

    answer = []

    for car_num, fee in arr:
        answer.append(fee)

    return answer