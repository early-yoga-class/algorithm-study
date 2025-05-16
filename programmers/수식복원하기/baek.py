def solution(exprs):
    res = []

    digits = [int(ch) for line in exprs for ch in line if '0' <= ch <= '9']
    bases = set(range(max(digits) + 1, 10))

    valids = set()
    for b in bases:
        ok = True
        for line in exprs:
            a, op, c, _, d = line.split()
            if d == 'X':
                continue
            if any(int(ch) >= b for ch in a + c + d if ch.isdigit()):
                ok = False
                break
            aa = int(a, b)
            cc = int(c, b)
            dd = int(d, b)
            if op == '+' and aa + cc != dd:
                ok = False
                break
            if op == '-' and aa - cc != dd:
                ok = False
                break
        if ok:
            valids.add(b)

    for line in exprs:
        a, op, c, _, d = line.split()
        if d != 'X':
            continue

        outs = set()
        for b in valids:
            if any(int(ch) >= b for ch in a + c if ch.isdigit()):
                continue
            aa = int(a, b)
            cc = int(c, b)
            rr = aa + cc if op == '+' else aa - cc
            if rr == 0:
                out = '0'
            else:
                out = ''
                while rr:
                    out = str(rr % b) + out
                    rr //= b
            outs.add(out)

        if len(outs) == 1:
            res.append(f"{a} {op} {c} = {outs.pop()}")
        else:
            res.append(f"{a} {op} {c} = ?")

    return res
