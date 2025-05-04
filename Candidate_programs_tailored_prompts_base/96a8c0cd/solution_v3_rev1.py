from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0]) if grid else 0
    out = [row[:] for row in grid]
    h_segs = {}
    for r in range(m):
        c = 0
        while c < n:
            if grid[r][c] != 0:
                col = grid[r][c]
                start = c
                while c + 1 < n and grid[r][c + 1] == col:
                    c += 1
                end = c
                length = end - start + 1
                if col == 2 or length >= 3:
                    h_segs.setdefault(r, []).append((start, end))
            c += 1
    v_segs = {}
    for c in range(n):
        r = 0
        while r < m:
            if grid[r][c] != 0:
                col = grid[r][c]
                start = r
                while r + 1 < m and grid[r + 1][c] == col:
                    r += 1
                end = r
                length = end - start + 1
                if col == 2 or length >= 3:
                    v_segs.setdefault(c, []).append((start, end))
            r += 1
    for r in h_segs:
        h_segs[r].sort()
    for c in v_segs:
        v_segs[c].sort()
    # row corridors
    for r in range(m):
        bounds = sorted({c for c in range(n) if grid[r][c] != 0})
        is_h = {c: any(s <= c <= e for s, e in h_segs.get(r, [])) for c in bounds}
        if not any(is_h.values()):
            continue
        first = next(i for i, c in enumerate(bounds) if is_h[c])
        for i in range(first, len(bounds) - 1):
            a, b = bounds[i], bounds[i + 1]
            for c in range(a + 1, b):
                if out[r][c] == 0:
                    out[r][c] = 2
    # column corridors
    for c in range(n):
        bounds = sorted({r for r in range(m) if grid[r][c] != 0})
        is_v = {r: any(s <= r <= e for s, e in v_segs.get(c, [])) for r in bounds}
        if not any(is_v.values()):
            continue
        first = next(i for i, r in enumerate(bounds) if is_v[r])
        for i in range(first, len(bounds) - 1):
            a, b = bounds[i], bounds[i + 1]
            for r in range(a + 1, b):
                if out[r][c] == 0:
                    out[r][c] = 2
    return out