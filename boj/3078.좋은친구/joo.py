import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

names = deque()
ans = 0

NN = [deque() for _ in range(21)]

for _ in range(N):
    names.append(len(sys.stdin.readline().strip()))

# print(names)

for i in range(N):
    # 현재 학생의 이름길이 확인
    name_length = names[i]
    
    # 자기랑 같은 이름애들이 앞서서 나왔는지 확인하고, 친한친구가 될 수 없는 거리에 있는애들 쳐내기
    while NN[name_length] and i - NN[name_length][0] > K:
        NN[name_length].popleft()
    
    # 남은애들은 친한친구니까 정답에 추가
    ans += len(NN[name_length])
    # print(f"ans: {ans}, NN: {NN[name_length]}, i: {i}")

    # 자기도 이름길이 그룹 합류
    NN[name_length].append(i)
            
print(ans)