from collections import Counter, defaultdict
def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(v for row in grid for v in row)
    bg = max(cnt, key=cnt.get)
    seeds = defaultdict(list)
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                seeds[v].append((r, c))
    A = None
    oriA = dA = None
    groupA = None
    for c, pts in seeds.items():
        diag = defaultdict(list)
        anti = defaultdict(list)
        for r, col in pts:
            diag[col - r].append((r, col))
            anti[r + col].append((r, col))
        for d, g in diag.items():
            if len(g) >= 2:
                A, oriA, dA, groupA = c, 'diag', d, g
                break
        if A is not None:
            break
        for s, g in anti.items():
            if len(g) >= 2:
                A, oriA, dA, groupA = c, 'anti', s, g
                break
        if A is not None:
            break
    B = next((c for c in seeds if c != A), None)
    out = [row[:] for row in grid]
    if A is not None:
        rs = [r for r, _ in groupA]
        r0, r1 = min(rs), max(rs)
        if oriA == 'diag':
            for r in range(r0, r1 + 1):
                c = r + dA
                if 0 <= c < w and out[r][c] == bg:
                    out[r][c] = A
        else:
            for r in range(r0, r1 + 1):
                c = dA - r
                if 0 <= c < w and out[r][c] == bg:
                    out[r][c] = A
    if B is not None:
        ks = set()
        for r, c in seeds[B]:
            if oriA == 'diag' and r + c == dA:
                ks.add(r + c)
            if oriA == 'anti' and c - r == dA:
                ks.add(c - r)
        for k in ks:
            if oriA == 'diag':
                # B is anti
                s = k
                r0 = max(0, s - (w - 1))
                r1 = min(h - 1, s)
                for r in range(r0, r1 + 1):
                    c = s - r
                    if 0 <= c < w and out[r][c] == bg:
                        out[r][c] = B
            else:
                # B is diag
                d = k
                r0 = max(0, -d)
                r1 = min(h - 1, w - 1 - d)
                for r in range(r0, r1 + 1):
                    c = r + d
                    if 0 <= c < w and out[r][c] == bg:
                        out[r][c] = B
    return out