import sys
import pprint


n , k =  list(map(int, sys.stdin.readline().split()))

attendant_score = []

for _ in range(n):
    a, b, c, d = list(map(int,sys.stdin.readline().split()))
    attendant_score.append((a,b,c,d))
    

# print(*attendant_score, sep='\n')

""" for score in attendant_score:
   print(score) """

# 금은동 내림차 순으로 정렬
attendant_score.sort(key=lambda x : (-x[1], -x[2], -x[3]))
# print(*attendant_score, sep='\n')

i = 1
prev_score = (0,0,0,0)
rank = 1
result = {}

# 성적을 의미하는 변수 rank를 만든 뒤
# 이전 스코어 기록해두고,
# 스코어가 같으면 rank 가 갱신되지 않도록 처리하여
# 동점인 경우 같은 rank를 가지도록 함.

for cont in attendant_score:
    if prev_score[1:] != cont[1:]:
        # print(prev_score)
        # print(cont)
        prev_score = cont
        rank = i

    result[cont[0]] = rank
    i +=1

print(result[k])

        











