# 백준 1744번 수 묶기

N = int(input())

pos = []
neg = [] # 0 포함
one_sum = 0 

for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num <= 0:
        neg.append(num)
    else:
        one_sum += 1

pos.sort(reverse=True)
neg.sort()

ans = 0

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        ans += pos[i] * pos[i+1]
else: 
    for i in range(0, len(pos)-1, 2):
        ans += pos[i] * pos[i+1]
    ans += pos[-1]

if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        ans += neg[i] * neg[i+1]
else: 
    for i in range(0, len(neg)-1, 2):
        ans += neg[i] * neg[i+1]
    ans += neg[-1]
    
ans += one_sum

print(ans)