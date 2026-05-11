from collections import defaultdict


def solution(gems):
    target = len(set(gems))
    count = defaultdict(int)
    left = 0
    answer = [1, len(gems)]
    min_length = len(gems)

    for right, gem in enumerate(gems):
        count[gem] += 1

        while len(count) == target:
            length = right - left + 1
            if length < min_length:
                min_length = length
                answer = [left + 1, right + 1]

            count[gems[left]] -= 1
            if count[gems[left]] == 0:
                del count[gems[left]]
            left += 1

    return answer
