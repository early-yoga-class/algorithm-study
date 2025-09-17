from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]


    for rates in product(discounts, repeat=len(emoticons)):
        prices = []
        for i in range(len(emoticons)):
            prices.append(emoticons[i] * (100 - rates[i]) // 100)
        
        plus_user = 0
        total_sell = 0
        
        for user in users:
            user_discount, max_price = user
            subtotal = 0
            
            for i in range(len(emoticons)):
                if rates[i] >= user_discount:
                    subtotal += prices[i]
                    
            if subtotal >= max_price:
                plus_user += 1
            else:
                total_sell += subtotal
        
        if (plus_user > answer[0]) or (plus_user == answer[0] and total_sell > answer[1]):
            answer[0] = plus_user
            answer[1] = total_sell
        
    return answer