import math

N = int(input())

def check(n):
    count = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            count += 1
            n //= i
        i += 1
    if n > 1:  # 마지막 남은 소수도 포함
        count += 1
    return count

cnt = check(N)
print(math.ceil(math.log2(cnt)))