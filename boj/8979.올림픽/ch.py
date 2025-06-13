import sys

# n 은 국가의 수, k는 알고싶은 국가
n, k = map(int, input().split())

nations = []
for _ in range(n):
    idx, gold, silver, bronze = map(int, input().split())

    #(gold, silver, bronze, idx, joint_rank)
    nations.append([gold, silver, bronze, idx, 0])

sorted_rank = sorted(nations, key = lambda x : (-x[0], -x[1], -x[2]))


for i in range(n):
    if sorted_rank[i][4] != 0: continue
    sorted_rank[i][4] = i + 1
    currentRank = i + 1
    for j in range(i + 1, n):
        # 중복 순위 이미 입력되어있는지 체크
        if sorted_rank[j][4] != 0: continue

        if (sorted_rank[i][0] == sorted_rank[j][0] and
                sorted_rank[i][1] == sorted_rank[j][1] and
                sorted_rank[i][2] == sorted_rank[j][2]):
            sorted_rank[j][4] = currentRank
        else:
            i = j
            break


for _, _, _, idx, joint in sorted_rank:
    if idx == k:
        print(joint)
        break
