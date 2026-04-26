from collections import deque

def solution(players, m, k):
    answer = 0
    
    scale_in = deque()
    
    for hour, player in enumerate(players):
        while scale_in and scale_in[0] <= hour:
            scale_in.popleft()
           
        need_cnt = player // m
        if need_cnt > len(scale_in):
            for i in range(need_cnt - len(scale_in)):
                scale_in.append(hour + k)
                answer += 1
    
    return answer