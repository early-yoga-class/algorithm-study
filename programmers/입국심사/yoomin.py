def solution(n, times):
    left = 1
    right = min(times) * n
    
    while(left <= right):
        mid = (left + right)//2
        total = sum(mid//t for t in times)
        
        if (total >= n):
            right = mid -1
        else:
            left = mid + 1
            
    return left
        