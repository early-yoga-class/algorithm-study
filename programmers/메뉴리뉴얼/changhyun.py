from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        menu = []
        for order in orders:
            sorted_order = sorted(order)
            
            for comb in combinations(sorted_order, c):
                menu.append(comb)
                
        cnt = {}
        for comb in menu:
            key = ''.join(comb)
            cnt[key] = cnt.get(key, 0) + 1
            
        if not cnt: continue
        
        max_cnt = max(cnt.values())
        
        if max_cnt < 2: continue
        
        for key, cnt in cnt.items():
            if cnt == max_cnt:            
                answer.append(key)
            
    return sorted(answer)