from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for i in course:
        combo_list = []

        for j in orders:
            sorted_order = sorted(j)
            for _ in combinations(sorted_order, i):
                combo_list.append(''.join(_))

        count = Counter(combo_list).most_common()

        # 가장 많이 주문된 조합들 중 2번 이상 등장한 것만 선택
        if count and count[0][1] > 1:
            max_count = count[0][1]
            for menu, freq in count:
                if freq == max_count:
                    result.append(menu)
                else:
                    break

    return sorted(result)