from collections import deque

def solution(players, m, k):
    answer = 0
    
    servers = deque()    # 큐: [(증설 수, 증설 시간)]
    cur_servers = 0
    
    for i in range(24):
        while servers:
            if i - servers[0][1] >= k:
                cur_servers -= servers[0][0]
                servers.popleft()
            else:
                break
            
        need = players[i] // m # i~i+1 증설 서버 수
        if need > cur_servers:
            temp = need - cur_servers
            cur_servers += temp
            answer += temp
            servers.append((temp, i))
            
    return answer