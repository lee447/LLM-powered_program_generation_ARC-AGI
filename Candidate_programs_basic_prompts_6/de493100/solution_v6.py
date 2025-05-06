from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    b = 7
    rows = [i for i in range(n) for j in range(m) if grid[i][j] == b]
    cols = [j for i in range(n) for j in range(m) if grid[i][j] == b]
    if not rows:
        return []
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    best = None
    best_set = set()
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr0 = r0 + dr * H if dr > 0 else r0 + dr * H
        cc0 = c0 + dc * W if dc > 0 else c0 + dc * W
        rr1 = rr0 + H - 1
        cc1 = cc0 + W - 1
        if 0 <= rr0 <= rr1 < n and 0 <= cc0 <= cc1 < m:
            vals = [grid[i][j] for i in range(rr0, rr1+1) for j in range(cc0, cc1+1)]
            if b in vals:
                continue
            s = set(vals)
            if len(s) > len(best_set):
                best_set = s
                best = (rr0, rr1, cc0, cc1)
    if best is None:
        return []
    rr0, rr1, cc0, cc1 = best
    return [grid[i][cc0:cc1+1] for i in range(rr0, rr1+1)]