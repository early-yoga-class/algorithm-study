import sys

N, K = map(int, sys.stdin.readline().split())
country = []
for _ in range(N):
    country.append(list(map(int, sys.stdin.readline().split())))

country.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

turn = 0  
count = 0  
g = s = b = -1  

for i in range(len(country)):
    num, gold, silver, bronze = country[i]

    if gold == g and silver == s and bronze == b:
        count += 1  
    else:
        turn += count  
        count = 1  
        g, s, b = gold, silver, bronze

    if num == K:
        print(turn + 1)
        break
