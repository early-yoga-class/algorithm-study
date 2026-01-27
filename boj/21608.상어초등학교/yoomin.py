import heapq
import sys

N = int(input())
lst = []
doubleN =N**2
# seats = [False]*(doubleN + 1)
result = [[False]*N for _ in range(N)]
sum = 0

for _ in range(doubleN):
    lst.append(list(map(int,sys.stdin.readline().split())))

def check(turn,likes):
    global sum
    rank = []
    for i in range(N):
        for j in range(N):
            if result[i][j]:
                continue

            cnt_l = 0
            cnt_b = 0
            di = [-1,1,0,0]
            dj = [0,0,1,-1]

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    neighbor = result[ni][nj]
                    if not neighbor:
                        cnt_b += 1
                    else:
                        if neighbor in likes:
                            cnt_l += 1
            if not rank:
                    heapq.heappush(rank,(-cnt_l,-cnt_b,i,j))
            else:
                if -rank[0][0] > cnt_l:
                    continue
                elif -rank[0][0] == cnt_l:
                        heapq.heappush(rank,(-cnt_l,-cnt_b,i,j))
                else:
                    rank = []
                    heapq.heappush(rank,(-cnt_l,-cnt_b,i,j))
    result[rank[0][2]][rank[0][3]] = turn
    if rank[0][0] == 0:
         return

for l in lst:
    check(l[0],l[1:])
    
lst.sort()

for i in range(N):
    for j in range(N):
        turn = result[i][j]
        di = [-1,1,0,0]
        dj = [0,0,1,-1]
        cnt_l = 0
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            if 0 <= ni < N and 0 <= nj < N:
                if result[ni][nj] in lst[turn-1][1:]:
                    cnt_l += 1

        if cnt_l == 0:
            sum += 0
        else:
            sum += 10**(cnt_l-1)
    
print(sum)