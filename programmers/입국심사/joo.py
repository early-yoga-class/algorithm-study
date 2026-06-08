def solution(n, times):
    times.sort()
    lo, hi = 1, times[0] * n  # hi는 혼자 다 하는 경우

    while lo < hi:
        mid = (lo + hi) // 2
        
        # mid분 동안 처리 가능한 총 인원
        total = sum(mid // t for t in times)
        
        if total >= n:
            hi = mid       
        else:
            lo = mid + 1  

    return lo