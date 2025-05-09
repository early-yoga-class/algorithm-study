# 소인수분해 해주고 나온 소수 개수를 2로 나눈 몫

import math
K = int(input())
count = 0

def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, n + 1):
        if primes[p]:
            prime_numbers.append(p)

    return prime_numbers

prime_list = eratosthenes(K)


if len(prime_list) == 1:
     print(0)
else:
    for i in prime_list:
        while K % i == 0:
            count += 1
            K //= i
            if K == 1:
                break
    print(int(math.ceil((math.log(count,2)))))
    
