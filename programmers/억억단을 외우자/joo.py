def solution(e, starts):
    
    divisor_count = [0] * (e + 1)
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            divisor_count[j] += 1
            
    suffix_max = [0] * (e + 2)
    suffix_max[e] = e  

    for i in range(e - 1, 0, -1):
        if divisor_count[i] >= divisor_count[suffix_max[i + 1]]:
            suffix_max[i] = i
        else:
            suffix_max[i] = suffix_max[i + 1]
                
    result = []
    
    for i in starts:
        result.append(suffix_max[i])
        
    return result