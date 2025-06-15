import sys

n = int(sys.stdin.readline().strip())

nums = []
stk = []
result = [0] * n
nums += list(map(int,sys.stdin.readline().split()))

for i in range(n-1,-1,-1):
    while stk and nums[i] >= stk[-1]:
        stk.pop()
    if not stk:
        result[i] = -1
    else:
        result[i] = stk[-1]

    stk.append(nums[i])

print(*result)

        
# print(nums)


