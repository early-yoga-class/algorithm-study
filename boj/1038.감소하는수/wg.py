import sys
from itertools import *
input = sys.stdin.readline

# 아 시발 N까지가 아니라 N 번째
# 9876543210 이 리스트의 마지막
N = int(input().strip())
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

declined_number = []


# 1. 조합으로 1~10자리 수 생성
for i in range(1, 11):
  numbers = list(combinations(digits, i))

  for elem in numbers:
    elem = list(reversed(elem))
    int_elem = int(''.join(map(str, elem)))
    declined_number.append(int_elem)

declined_number.sort()

if N >= len(declined_number):
  print(-1)
else:
  print(declined_number[N])
