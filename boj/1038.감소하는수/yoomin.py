from itertools import combinations

N = int(input())
lst = list(range(10))
nums = []
for i in range(1,11):
    for com in combinations(lst,i):
        nums.append(int(''.join(list(map(str,sorted(com,reverse=True))))))
nums.sort()

if (N>=len(nums)):
    print(-1)
else:
    print(nums[N])