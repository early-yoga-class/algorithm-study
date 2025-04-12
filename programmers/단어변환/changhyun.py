answer = 0

def solution(begin, target, words):
    #----- 타겟을 포함하고 있는지 체크
    wordContain = False
    for word in words:
        if word == target:
            wordContain = True
    if not wordContain: return 0

    # 한번에 한개의 알파벳만 바꿀 수 있다
    # words에 있는 단어로만 변환할 수 있다
    
    visited = [False] * len(words)
    # words.sort()
    
    def word_count_check(word, target):
        cnt = 0
        for i in range(len(word)):
            if word[i] != target[i]:
                cnt += 1
        return cnt == 1
    
    def dfs(current, count):
        global answer
        if current == target:
            answer = count
            print(answer, current, count)
            return
        for idx, word in enumerate(words):
            # 방문하지 않았고 둘의 단어 차이가 2개이상 나지 않으면
            if not visited[idx] and word_count_check(current, word):
                visited[idx] = True
                dfs(word, count + 1)
                # visited[idx] = False
                
    dfs(begin, 0)
    return answer