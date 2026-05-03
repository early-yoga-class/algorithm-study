from collections import defaultdict

def solution(gems):
    total_types = len(set(gems))
    gem_count = defaultdict(int)
    current_types = 0
    left = 0
    min_len = float('inf')
    result = [0, 0]

    for right in range(len(gems)):
        gem = gems[right]
        if gem_count[gem] == 0:
            current_types += 1
        gem_count[gem] += 1

        while current_types == total_types:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                result = [left + 1, right + 1]  # 1-indexed

            left_gem = gems[left]
            gem_count[left_gem] -= 1
            if gem_count[left_gem] == 0:
                current_types -= 1
            left += 1

    return result
