from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    segs = []
    for j in range(w):
        i = 0
        while i < h-2:
            E = grid[i][j]
            C = grid[i+1][j]
            if E != 0 and C != 0 and C != E:
                r = i+2
                while r < h and grid[r][j] == C:
                    r += 1
                if r < h and grid[r][j] == E and r - i - 1 >= 1:
                    segs.append((j, i, r, C, E, r - i - 1))
                    i = r
                    continue
            i += 1
    if len(segs) < 2:
        return [row[:] for row in grid]
    j1, i1, k1, C1, E1, L1 = segs[0]
    j2, i2, k2, C2, E2, L2 = segs[1]
    odd1, odd2 = L1 % 2, L2 % 2
    if odd1 != odd2:
        pick = 0 if odd1 else 1
    elif odd1 == 1 and odd2 == 1:
        pick = 0 if L1 < L2 else 1
    else:
        pick = 0 if E1 < E2 else 1
    j0, i0, k0, C0, E0, L0 = segs[pick]
    plain = []
    for j in range(w):
        if j == j0:
            continue
        col = [grid[r][j] for r in range(h) if grid[r][j] != 0]
        if len(col) >= L0 + 2 and all(v == E0 for v in col):
            plain.append(j)
    out = [row[:] for row in grid]
    if plain:
        jP = max(plain, key=lambda j: sum(1 for r in range(h) if grid[r][j] == E0))
        rows = [r for r in range(h) if grid[r][jP] == E0]
        if rows:
            s, e = min(rows), max(rows)
            for r in range(s+1, e):
                out[r][jP] = C0
    for r in range(i0+1, k0):
        out[r][j0] = E0
    return out