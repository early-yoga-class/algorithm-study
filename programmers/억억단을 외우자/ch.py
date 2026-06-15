def 약수의개수계산(end):
    counts = [0] * (end + 1)
    
    for i in range(1, end + 1):
        for j in range(i, end + 1, i):
            counts[j] += 1 
            
    return counts


def solution(e, starts):
    answer = []
    counts = 약수의개수계산(e)
    start_range_indexes = [0] * (e + 1)
    max_count = 0
    max_idx = e
    for idx in range(e, 0, -1):
        if counts[idx] >= max_count:
            max_count = counts[idx]
            max_idx = idx
            
        start_range_indexes[idx] = max_idx
        
    return [start_range_indexes[s] for s in starts]