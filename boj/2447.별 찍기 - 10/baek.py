# 백준 별 찍기 - 10

def recursive(n):
    if n == 1:
        return ['*']
    else:
        stars = recursive(n//3)
        result = []
        for _ in stars:
            result.append(_*3)
        for _ in stars:
            result.append(_ +' '*(n//3)+ _)
        for _ in stars:
            result.append(_*3)

        return result

N = int(input())
print('\n'.join(recursive(N)))