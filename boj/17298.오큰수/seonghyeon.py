from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
result = [-1 for i in range(n)]
stack = deque()
num = list(map(int, input().split()))

for i in range(n):
    while stack and num[stack[-1]] < num[i]:
        idx = stack.pop()
        result[idx] = num[i]
    stack.append(i)

print(" ".join(map(str, result)))