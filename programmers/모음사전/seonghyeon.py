def cal(offset, idx):
    numbers = [625, 125, 25, 5, 1]
    sumNum = 0
    for i in range(idx, 5):
        sumNum += (numbers[i] * offset)

    return sumNum + 1


def solution(word):
    answer = 0
    diction = {
        "A": 0,
        "E": 1,
        "I": 2,
        "O": 3,
        "U": 4
    }

    for i in range(len(word)):
        answer += cal(diction[word[i]], i)
    return answer