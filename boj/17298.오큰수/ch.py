import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

stack = []
answer = deque()

target = list(map(int, input().split()))

for i in range(len(target) - 1, -1, -1):
    current = target[i]

    while stack and stack[-1] < current:
        stack.pop()

    if len(stack) == 0:
        answer.appendleft(-1)
    else:
        answer.appendleft(stack[-1])
        
    stack.append(current)

print(" ".join(str(num) for num in answer))