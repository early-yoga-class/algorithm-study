import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(permutations(list(range(1, 10)), 3))	# 1부터 9까지의 3자리 숫자 모음 생성

for _ in range(n):
    num, s, b = map(int, input().split())
    tmp = []	# 현재 조건에 맞는 숫자 모음
    
    for check in nums:
        cnt_s, cnt_b = 0, 0	# 스트라이크와 볼의 갯수

        for i, str_num in enumerate(str(num)):	
            if int(str_num) == check[i]:		
                cnt_s += 1						
            if int(str_num) != check[i] and int(str_num) in check:
                cnt_b += 1						

        if s == cnt_s and b == cnt_b:			
            tmp.append(check)					
    nums = tmp									

print(len(nums))							