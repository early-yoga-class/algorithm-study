from collections import defaultdict
def solution(gems):
    total = len(set(gems))
    now = 0
    gems_dict = defaultdict(int)
    left = 0
    min_len = float('inf')
    
    answer = []
    for right in range(len(gems)):
        if (gems_dict[gems[right]] == 0) :
            now += 1
        gems_dict[gems[right]] += 1
        if (total == now):
            while(left <= right):
                now_len = right-left+1
                if (min_len > now_len):
                    answer = [left+1,right+1]
                    min_len = now_len
                if (gems_dict[gems[left]] == 1):
                    break
                else:
                    gems_dict[gems[left]] -= 1
                    left += 1
                    
    return answer