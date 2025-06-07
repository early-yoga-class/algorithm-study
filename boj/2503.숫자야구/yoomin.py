n = int(input())
q = []
cnt = 0
for _ in range(n):
    x = input().split()
    s, a, b = x[0], int(x[1]), int(x[2])
    q.append([s,a,b])
for i in range(123, 988):
    si = str(i)
    if len(set(si+'0')) < 4:
        continue
    for j in range(n):
        st = 0
        bo = 0
        for k in range(3):
            for l in range(3):
                if si[l] == q[j][0][k]:
                    if k == l:
                        st += 1
                    else:
                        bo += 1
        if st != q[j][1] or bo != q[j][2]:
            break
    else:
        cnt += 1
print(cnt)                