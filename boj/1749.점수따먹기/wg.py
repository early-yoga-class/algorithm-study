import sys

input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

num = [[0]  * (m+1)]

for i in range(n):
  num_row = [0] + list(map(int, input().rstrip().split()))
  num.append(num_row)

sum_num = [[0]  * (m+1) for _ in range(n+1)]

max_num = -10000

for i in range(1,n+1):
  for j in range(1,m+1):
    sum_num[i][j] = sum_num[i-1][j] + sum_num[i][j-1] - sum_num[i-1][j-1] + num[i][j]

for x1 in range(1,n+1):
  for y1 in range(1,m+1):
    for x2 in range(1,x1+1):
      for y2 in range(1,y1+1):
        test = sum_num[x1][y1] - sum_num[x1][y2-1] - sum_num[x2-1][y1] + sum_num[x2-1][y2-1]
        max_num = max(max_num, test)

print(max_num)
