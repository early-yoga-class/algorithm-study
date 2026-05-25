from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    d_time, d_price, u_time, u_price = fees
    
    # 누적 시간 {car_number : [in_time, acc_time]}
    user_time_list = defaultdict(lambda: [None, 0])
    
    # 입차 목록(car_number)
    in_list = set()
        
    def time_convert(time):
        hour, minute = map(int, time.split(":"))
        return hour * 60 + minute
        
    def price_cal(acc_time):
        if acc_time <= d_time: return d_time
        return d_time + math.ceil((acc_time - d_time) / u_time) * u_price
        
    
    for record in records:
        time, car_number, state = record.split(" ")
        
        if state == "IN":
            in_list.add(car_number)
            user_time_list[car_number][0] = time
        else:
            in_list.remove(car_number)
            in_time = user_time_list[car_number][0]
            user_time_list[car_number][1] += time_convert(time) - time_convert(in_time)
            user_time_list[car_number][0] = None
            
    # 출차 안했으면 23:59 출차
    for car_number in in_list:
        user_time_list[car_number][1] += time_convert("23:59") - time_convert(user_time_list[car_number][0])
        user_time_list[car_number][0] = None
    
    for car_number in sorted(user_time_list.keys()):
        answer.append(price_cal(user_time_list[car_number][1]))
    

    return answer