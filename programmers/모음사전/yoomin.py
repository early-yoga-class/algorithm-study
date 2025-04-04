def solution(word):
    answer = 0
    weights = [781, 156, 31, 6, 1]  
    chars = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    for i, ch in enumerate(word):
        answer += chars[ch] * weights[i] + 1  
    return answer
