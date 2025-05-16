import re
from collections import Counter

def solution(expressions):
    # 1) 알려진 식으로 전역 진법 후보 좁히기
    bases = set(range(2, 10))
    for exp in expressions:
        A, op, B, _, C = exp.split()
        if C == 'X': continue
        digits = re.findall(r'\d', A + B + C)
        min_base = max(2, max(map(int, digits)) + 1)

        valid = set()
        for b in bases:
            if b < min_base: continue
            try:
                a, bb, cc = int(A, b), int(B, b), int(C, b)
            except ValueError:
                continue
            if (op == '+' and a + bb == cc) or (op == '-' and a - bb == cc):
                valid.add(b)
        bases &= valid

    # 10진→b진 변환 헬퍼
    def to_base(n, b):
        if n == 0: return '0'
        digs = []
        while n:
            digs.append(str(n % b))
            n //= b
        return ''.join(reversed(digs))

    # X 식 모으기
    x_list = [(i, exp) for i, exp in enumerate(expressions) if exp.split()[4] == 'X']
    fill = {}
    pending = x_list.copy()

    # (1) “유일한 답”이 나오는 식부터 처리하며 진법 좁히기
    changed = True
    while changed:
        changed = False
        for idx, exp in pending:
            A, op, B, _, _ = exp.split()
            digits = re.findall(r'\d', A + B)
            min_base = max(2, max(map(int, digits)) + 1)

            # 각 진법 b에서의 결과 문자열 수집
            rep = {}
            for b in bases:
                if b < min_base: continue
                try:
                    a, bb = int(A, b), int(B, b)
                except ValueError:
                    continue
                res = a + bb if op == '+' else a - bb
                rep[b] = to_base(res, b)

            # 결과가 하나로 고정되면 그 값으로 채우고 진법 좁히기
            repset = set(rep.values())
            if len(rep) > 0 and len(repset) == 1:
                val = repset.pop()
                fill[idx] = val
                # 이 결과를 내는 진법만 남기기
                bases = {b for b, v in rep.items() if v == val}
                pending.remove((idx, exp))
                changed = True
                break

    # (2) 나머지 식은 최종 진법 집합에서 유일하면 채우고, 아니면 '?' 
    for idx, exp in pending:
        A, op, B, _, _ = exp.split()
        digits = re.findall(r'\d', A + B)
        min_base = max(2, max(map(int, digits)) + 1)

        rep = {}
        for b in bases:
            if b < min_base: continue
            try:
                a, bb = int(A, b), int(B, b)
            except ValueError:
                continue
            res = a + bb if op == '+' else a - bb
            rep[b] = to_base(res, b)

        repset = set(rep.values())
        fill[idx] = repset.pop() if len(repset) == 1 else '?'

    # 결과 문자열 조합
    answer = []
    j = 0
    for exp in expressions:
        A, op, B, _, C = exp.split()
        if C == 'X':
            answer.append(f"{A} {op} {B} = {fill[x_list[j][0]]}")
            j += 1
    return answer