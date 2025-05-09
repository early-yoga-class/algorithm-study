
import math

k = int(input())

nums = [i for i in range(k+1)]
visit = [False for _ in range(k+1)]
visit[0]=True
visit[1]=True

prime = list()

for num in range(2, k+1):
    if not visit[num]:
        prime.append(num)
        for multiple in range(num*num, k+1, num):
            visit[multiple] = True
count = 0

for i in prime:
    while k % i == 0:
        count += 1
        k//=i
    i+=1
if k>1:
    count += 1

print(math.ceil(math.log2(count)))

