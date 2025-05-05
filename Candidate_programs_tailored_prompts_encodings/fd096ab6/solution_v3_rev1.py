from collections import Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(c for row in grid for c in row)
    bg = counts.most_common(1)[0][0]
    out = [row[:] for row in grid]
    cells = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != bg:
                cells.setdefault(v, []).append((i, j))
    for v, pts in cells.items():
        rs = [r for r, _ in pts]
        cs = [c for _, c in pts]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        if r1 - r0 == 1 and c1 - c0 == 1:
            for r in (r0, r1):
                for c in (c0, c1):
                    out[r][c] = v
    return out