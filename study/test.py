from collections import defaultdict

#column
#k

n = len(column)
count = defaultdict(int)
k_cnt = 0

for i in range(n):
    for j in range(n):
        if column[i][j] == k:
            count['x'+str(i)] += 1
            count['y'+str(j)] += 1
            k_cnt += 1

sum = 0
while (k_cnt > 0):
    key = max(count, key = count.get)
    col, a = key[0],int(key[1])
    if col == 'x':
        for j in range(n):
            if column[a][j] == k:
                count['x'+str(a)] -= 1
                count['y'+str(j)] -= 1
                k_cnt -= 1
    else:
        for i in range(n):
            if column[i][a] == k:
                count['x'+str(i)] -= 1
                count['y'+str(a)] -= 1
                k_cnt -= 1
    sum += 1

print(sum)