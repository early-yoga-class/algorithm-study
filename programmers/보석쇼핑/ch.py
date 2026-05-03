from collections import defaultdict

def solution(gems):
    """
    checked = set(gems)
    answer = []
    left = 0

    for right in range(len(gems)):
        while left < right and gems[left] in gems[left + 1:right + 1]:
            left += 1

        if right - left + 1 >= len(checked):
            current_gems = set(gems[left:right + 1])

            if current_gems == checked:
                answer.append([left + 1, right + 1])

    answer.sort(key=lambda x: ((x[1] - x[0]), x[0]))

    return answer[0]
    """

    checked = set(gems)
    answer = [0, len(gems) - 1]
    current_gems = defaultdict(int)
    left = 0

    for right in range(len(gems)):
        current_gems[gems[right]] += 1  
        
        while len(current_gems) >= len(checked):
            # 최단 구간 갱신
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            current_gems[gems[left]] -= 1
            
            if current_gems[gems[left]] == 0:
                del current_gems[gems[left]]
            
            left += 1

    return [answer[0] + 1, answer[1] + 1]