from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    rows5 = sorted({r for r in range(H) for c in range(W) if grid[r][c] == 5})
    cols5 = sorted({c for r in range(H) for c in range(W) if grid[r][c] == 5})
    def groups(sorted_list):
        gs, cur = [], []
        for x in sorted_list:
            if not cur or x == cur[-1] + 1:
                cur.append(x)
            else:
                gs.append(cur)
                cur = [x]
        if cur:
            gs.append(cur)
        return gs
    rg = groups(rows5)
    cg = groups(cols5)
    ys = [g[0] for g in rg]
    xs = [g[0] for g in cg]
    h = len(rg[0])
    w = len(cg[0])
    y0, y1 = ys[0], ys[-1]
    x0, x1 = xs[0], xs[-1]
    region_rs = set(range(y0, y1 + h))
    region_cs = set(range(x0, x1 + w))
    stripe_rows = [r for r in range(y0, y1 + h) if r not in set(rows5)]
    stripe_cols = [c for c in range(x0, x1 + w) if c not in set(cols5)]
    ans = [row[:] for row in grid]
    for r in stripe_rows:
        for c in range(W):
            if ans[r][c] == 0:
                ans[r][c] = 2 if c in region_cs else 1
    for c in stripe_cols:
        for r in range(H):
            if ans[r][c] == 0:
                ans[r][c] = 2 if r in region_rs else 1
    return ans