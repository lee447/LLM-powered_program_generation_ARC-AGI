from collections import Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(v for row in grid for v in row)
    bg = cnt.most_common(1)[0][0]
    seeds = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                seeds.setdefault(v, []).append((r, c))
    A = None
    oriA = keyA = None
    groupA = None
    for v, pts in seeds.items():
        diag = {}
        anti = {}
        for r, c in pts:
            diag.setdefault(c - r, []).append((r, c))
            anti.setdefault(r + c, []).append((r, c))
        for d, g in diag.items():
            if len(g) >= 2:
                A, oriA, keyA, groupA = v, 'diag', d, g
                break
        if A is not None:
            break
        for s, g in anti.items():
            if len(g) >= 2:
                A, oriA, keyA, groupA = v, 'anti', s, g
                break
        if A is not None:
            break
    if A is None:
        for v, pts in seeds.items():
            if len(pts) >= 2:
                (r1, c1), (r2, c2) = pts[:2]
                if c1 - r1 == c2 - r2:
                    A, oriA, keyA, groupA = v, 'diag', c1 - r1, [(r1, c1), (r2, c2)]
                else:
                    A, oriA, keyA, groupA = v, 'anti', r1 + c1, [(r1, c1), (r2, c2)]
                break
    B = next((v for v in seeds if v != A), None)
    out = [row[:] for row in grid]
    rs = [r for r, _ in groupA]
    r0, r1 = min(rs), max(rs)
    if oriA == 'diag':
        for r in range(r0, r1 + 1):
            c = r + keyA
            if 0 <= c < w and out[r][c] == bg:
                out[r][c] = A
    else:
        for r in range(r0, r1 + 1):
            c = keyA - r
            if 0 <= c < w and out[r][c] == bg:
                out[r][c] = A
    if B is not None:
        keysB = []
        for r, c in seeds[B]:
            if oriA == 'diag' and c - r == keyA:
                keysB.append(r + c)
            if oriA == 'anti' and r + c == keyA:
                keysB.append(c - r)
        for key in set(keysB):
            if oriA == 'diag':
                r_start = max(0, key - (w - 1))
                r_end = min(h - 1, key)
                for r in range(r_start, r_end + 1):
                    c = key - r
                    if out[r][c] == bg:
                        out[r][c] = B
            else:
                r_start = max(0, -key)
                r_end = min(h - 1, w - 1 - key)
                for r in range(r_start, r_end + 1):
                    c = r + key
                    if out[r][c] == bg:
                        out[r][c] = B
    return out