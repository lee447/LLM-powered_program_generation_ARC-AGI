def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    types = []
    for r in range(h):
        nonzeros = [c for c in grid[r] if c != 0]
        us = set(nonzeros)
        if len(us) <= 1:
            v = us.pop() if us else 0
            types.append(('bg', v))
        else:
            row = grid[r]
            try:
                z = row.index(0)
                segment = row[:z]
            except ValueError:
                segment = row[:]
            L = len(segment)
            p = L
            for cand in range(1, L + 1):
                ok = True
                for i in range(L - cand):
                    if segment[i] != segment[i + cand]:
                        ok = False
                        break
                if ok:
                    p = cand
                    break
            pattern = segment[:p]
            types.append(('pattern', pattern))
    for r in range(h):
        tp, val = types[r]
        if tp == 'bg':
            for c in range(w):
                if res[r][c] == 0:
                    res[r][c] = val
        else:
            pattern = val
            p = len(pattern)
            for c in range(w):
                if res[r][c] == 0:
                    res[r][c] = pattern[c % p]
    return res