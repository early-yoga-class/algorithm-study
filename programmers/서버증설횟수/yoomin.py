import heapq

def added_num(user,m,server_num):
    x = 0
    while(True):
        if (x*m <= user < (x+1)*m):
            break
        x+=1
    if x > server_num:
        return (x-server_num)
    else:
        return 0

def solution(players, m, k):
    s_sum = 0
    added_count = 0
    n = 0
    servers = []
    
    while(n < 24):
        while(servers and servers[0] <= n):
            heapq.heappop(servers)
            s_sum -= 1
            
        num = added_num(players[n],m,s_sum)
        if num > 0:
            for _ in range(num):
                heapq.heappush(servers,n+k)
            added_count += num
            s_sum += num     
        n+=1
        

    return added_count