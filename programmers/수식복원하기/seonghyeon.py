def solution(expressions):
    def to_decimal(s, base):
        try:
            return int(s, base)
        except:
            return None

    min_base = 2
    for expr in expressions:
        parts = expr.replace('=', ' = ').split()
        for part in parts:
            if part not in ['+', '-', '=', 'X']:
                min_base = max(min_base, max(int(ch) for ch in part) + 1)

    valid_bases = []
    for base in range(min_base, 10):
        valid = True
        for expr in expressions:
            if 'X' in expr:
                continue
            a, op, b, _, c = expr.replace('=', ' = ').split()
            a_dec = to_decimal(a, base)
            b_dec = to_decimal(b, base)
            c_dec = to_decimal(c, base)
            if None in [a_dec, b_dec, c_dec]:
                valid = False
                break
            if op == '+' and a_dec + b_dec != c_dec:
                valid = False
                break
            if op == '-' and a_dec - b_dec != c_dec:
                valid = False
                break
        if valid:
            valid_bases.append(base)

    answer = []
    for expr in expressions:
        if 'X' not in expr:
            continue
        a, op, b, _, _ = expr.replace('=', ' = ').split()
        results = set()
        for base in valid_bases:
            a_dec = to_decimal(a, base)
            b_dec = to_decimal(b, base)
            if None in [a_dec, b_dec]:
                continue
            if op == '+':
                res = a_dec + b_dec
            else:
                res = a_dec - b_dec
            if res < 0:
                continue
            res_str = ''
            temp = res
            if temp == 0:
                res_str = '0'
            else:
                while temp > 0:
                    res_str = str(temp % base) + res_str
                    temp //= base
            results.add(res_str)
        if len(results) == 1:
            result = results.pop()
        else:
            result = '?'
        answer.append(f"{a} {op} {b} = {result}")
    return answer