from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe_positions = {}
    for y in range(h):
        for x in range(w):
            v = grid[y][x]
            if v != 0 and v != 8:
                stripe_positions[x] = v
    stripe_items = sorted(stripe_positions.items(), key=lambda t: t[0])
    stripe_xs = [x for x, _ in stripe_items]
    stripe_colors = [c for _, c in stripe_items]
    shape_xs = sorted({x for y in range(h) for x in range(w) if grid[y][x] == 8})
    x_min, x_max = shape_xs[0], shape_xs[-1]
    shape_mid = (x_min + x_max) / 2
    stripe_mid = sum(stripe_xs) / len(stripe_xs)
    dx = shape_mid - stripe_mid
    cents = [sx + dx for sx in stripe_xs]
    out = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 8:
                ds = [abs(x - c) for c in cents]
                m = min(ds)
                idxs = [i for i,d in enumerate(ds) if d == m]
                if len(idxs) > 1:
                    gt = [i for i in idxs if cents[i] >= x]
                    idx = max(gt) if gt else min(idxs)
                else:
                    idx = idxs[0]
                out[y][x] = stripe_colors[idx]
    return out