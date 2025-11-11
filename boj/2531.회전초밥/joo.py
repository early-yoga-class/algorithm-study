
n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]


sushi_count = {}
max_variety = 0


for i in range(k):
    if belt[i] in sushi_count:
        sushi_count[belt[i]] += 1
    else:
        sushi_count[belt[i]] = 1

for i in range(n):
    current_variety = len(sushi_count)

    if c not in sushi_count:
        current_variety += 1
    
    max_variety = max(max_variety, current_variety)
    
    left_sushi = belt[i]
    sushi_count[left_sushi] -= 1
    
    if sushi_count[left_sushi] == 0:
        del sushi_count[left_sushi]
    
    right_sushi = belt[(i + k) % n]
    
    if right_sushi in sushi_count:
        sushi_count[right_sushi] += 1
    else:
        sushi_count[right_sushi] = 1

print(max_variety)