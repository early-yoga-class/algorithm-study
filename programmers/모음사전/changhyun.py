vowels = ['A', 'E', 'I', 'O' ,'U']
answer = 0
idx = -1

def solution(word):
    def permutation(k, selected):
        global idx, answer
        if k <= 5:
            idx += 1
            if selected == word:
                answer = idx
        else:
            return
        for i in range(5):
            permutation(k + 1, selected + vowels[i])
    permutation(0, "")
    return answer