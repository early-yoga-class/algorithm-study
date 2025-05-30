from itertools import combinations

def solution(orders, course):
    menu = {}
    result = []
    for order in orders:
        order = sorted(order)
        for num in course:
            for comb in combinations(order,num):
                comb = ''.join(comb)
                menu[comb] = menu.get(comb,0) + 1
    
    for num in course:
        max_count = 0
        for k in menu:
            if len(k) == num and menu[k] >=2 :
                max_count = max(max_count,menu[k])
        if max_count == 0:
            continue
            
  
        for k in menu:
            if len(k) == num and menu[k] == max_count:
                result.append(k)
        result = sorted(result)
                
        

    return result