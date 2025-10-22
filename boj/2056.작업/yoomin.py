import sys

N = int(input())
times = [None]
for _ in range(N):
    jobs = list(map(int,sys.stdin.readline().split()))
    
    if jobs[1] == 0:
        times.append((0,jobs[0]))
    
    else:
        duration = jobs[0]
        number = jobs[1]
        last_time = -1
        
        for pri in jobs[2:]:
            last_time = max(last_time,times[pri][1])
        
        times.append((last_time,last_time + duration))

max_time = -1

for time in times:
    if time == None:
        continue
    max_time = max(time[1],max_time)

print(max_time)