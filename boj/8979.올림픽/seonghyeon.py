n, k = map(int, input().split())

result = [list(map(int, input().split())) for _ in range(n)]

rank = sorted(result, key= lambda x : (-x[1],-x[2],-x[3]))

def diff(a, b):
    for i in range(1,4):
        if a[i] == b[i]:
            continue
        else:
            return False
    return True

target = list()
for r in rank:
    if r[0] == k:
        target = r
        break

ranking = 1
for r in rank:
    if r[0] != k:
        if not diff(target, r):
            ranking+=1
            continue
        else:
            continue
    elif r[0] == k:
        print(ranking)
        break

