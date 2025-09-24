# 백준 1094번 막대기

sticks = [2**i for i in range(6, -1, -1)]
goal = int(input())
count = 0
temp = 0

for i in sticks:
    if goal == temp :
        break
    
    if temp + i <= goal:
        temp += i
        count += 1

print(count)
