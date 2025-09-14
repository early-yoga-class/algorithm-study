from itertools import product

def solution(users, emoticons):
    # 가능한 할인율
    rates = [10, 20, 30, 40]
    # 이모티콘별 할인 가격
    discounted = [
        [price * (100 - r) // 100 for r in rates]  # 길이 4
        for price in emoticons
    ]

    best_sub = -1
    best_revenue = -1

    # 모든 할인 조합 탐색 (각 이모티콘에 대해 인덱스 0~3 -> 10/20/30/40%)
    # (이모티콘1 할인율, 이모티콘2 할인율, ...., 이모티콘n 할인율)
    for choice in product(range(4), repeat=len(emoticons)):
        subs = 0
        revenue = 0

        # 각 유저 평가
        for need_rate, limit in users:
            basket = 0
            # 선택된 할인 인덱스 choice[i]가 가리키는 실제 할인율
            for i, idx in enumerate(choice):
                applied_rate = rates[idx]
                # 할인율이 구매전환을위한 할인율만큼 높으면
                if applied_rate >= need_rate:
                    # 장바구니에 쌓고
                    basket += discounted[i][idx]
            # 장바구니에 구독임계만큼 쌓이면 구독으로 전환
            if basket >= limit:
                subs += 1
            else:
                # 구독 안하면 매출에 포함
                revenue += basket

        # (가입자, 매출) 사전식 최대
        if (subs, revenue) > (best_sub, best_revenue):
            best_sub, best_revenue = subs, revenue

    return [best_sub, best_revenue]
