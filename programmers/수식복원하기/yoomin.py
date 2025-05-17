def solution(expressions):
    # n진법 문자열 → 10진수
    def to10(n, s):
        total = 0
        for i, ch in enumerate(reversed(s)):
            total += int(ch) * (n ** i)
        return total

    # 10진수 → n진법 문자열
    def toN(n, x):
        if x == 0:
            return '0'
        res = ''
        while x > 0:
            res = str(x % n) + res
            x //= n
        return res

    # 1) 모든 수식(A, B)에서 등장한 숫자로 최소 진법 결정
    max_digit = 0
    for expr in expressions:
        left, _ = expr.split('=')
        a, _, b = left.strip().split()
        for ch in a + b:
            max_digit = max(max_digit, int(ch))
    min_base = max(2, max_digit + 1)

    # 2) 알려진 수식(= X가 아닌)만 보고 후보 진법 추리
    candidates = []
    for base in range(min_base, 10):
        ok = True
        for expr in expressions:
            if expr.endswith('= X'):
                continue
            left, right = expr.split('=')
            a, op, b = left.strip().split()
            c = right.strip()
            # A, B, C 모두 digit<base 여야 함
            if any(int(d) >= base for d in a + b + c):
                ok = False
                break
            a10, b10, c10 = to10(base, a), to10(base, b), to10(base, c)
            if op == '+' and a10 + b10 != c10:
                ok = False
                break
            if op == '-' and a10 - b10 != c10:
                ok = False
                break
        if ok:
            candidates.append(base)

    # 3) = X 수식들 복원
    answer = []
    for expr in expressions:
        if not expr.endswith('= X'):
            continue
        left, _ = expr.split('=')
        a, op, b = left.strip().split()
        results = set()
        for base in candidates:
            # A, B digit<base 체크
            if any(int(d) >= base for d in a + b):
                continue
            a10, b10 = to10(base, a), to10(base, b)
            val10 = a10 + b10 if op == '+' else a10 - b10
            results.add(toN(base, val10))

        # 유일하면 그 값, 아니면 ?
        if len(results) == 1:
            answer.append(f"{a} {op} {b} = {results.pop()}")
        else:
            answer.append(f"{a} {op} {b} = ?")

    return answer
