from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    anchors = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    if len(anchors) == 4:
        rows = sorted({r for r, _ in anchors})
        cols = sorted({c for _, c in anchors})
        if len(rows) == 2 and len(cols) == 2:
            r1, r2 = rows
            stripe_cols = cols
            seq = [grid[r][stripe_cols[0]] for r in range(r1 + 1, r2)]
            stripe_colors = sorted({v for v in seq})
            targets = sorted([c for c in [0, 6, 7, 8] if c not in stripe_colors])
            if len(stripe_colors) == 2 and len(targets) == 2:
                m = {stripe_colors[0]: targets[1], stripe_colors[1]: targets[0]}
                for c in stripe_cols:
                    for r in range(r1 + 1, r2):
                        v = grid[r][c]
                        if v in m:
                            res[r][c] = m[v]
                return res
    stripe_rows = [r for r in range(h) if sum(grid[r][c] == 4 for c in range(w)) == 2]
    if stripe_rows:
        stripe_rows.sort()
        r0 = stripe_rows[0]
        cols0 = sorted(c for c in range(w) if grid[r0][c] == 4)
        c1, c2 = cols0
        seq = grid[r0][c1+1:c2]
        stripe_colors = sorted({v for v in seq})
        targets = sorted([c for c in [0, 6, 7, 8] if c not in stripe_colors])
        if len(stripe_colors) == 2 and len(targets) == 2:
            m = {stripe_colors[0]: targets[1], stripe_colors[1]: targets[0]}
            for r in stripe_rows:
                colsr = sorted(c for c in range(w) if grid[r][c] == 4)
                c1r, c2r = colsr
                for c in range(c1r+1, c2r):
                    v = grid[r][c]
                    if v in m:
                        res[r][c] = m[v]
    return res