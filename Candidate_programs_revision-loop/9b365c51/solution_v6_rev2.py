from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe_x = []
    stripe_cols = []
    for c in range(w):
        col = [grid[r][c] for r in range(h)]
        if all(v not in (0, 8) for v in col):
            stripe_x.append(c)
            stripe_cols.append(col[0])
    n = len(stripe_cols)
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    if not cells or n == 0:
        return [[0] * w for _ in range(h)]
    cells_sorted = sorted(cells, key=lambda x: x[1])
    m = len(cells)
    centers = []
    for i in range(n):
        idx = int(i * (m - 1) / (n - 1)) if n > 1 else m // 2
        centers.append((cells_sorted[idx][0], cells_sorted[idx][1]))
    for _ in range(10):
        clusters = [[] for _ in range(n)]
        for r, c in cells:
            best, bd = 0, abs(r - centers[0][0]) + abs(c - centers[0][1])
            for i in range(1, n):
                d = abs(r - centers[i][0]) + abs(c - centers[i][1])
                if d < bd:
                    bd, best = d, i
            clusters[best].append((r, c))
        new_centers = []
        for i, cl in enumerate(clusters):
            if cl:
                rs = sum(p[0] for p in cl) / len(cl)
                cs = sum(p[1] for p in cl) / len(cl)
                new_centers.append((rs, cs))
            else:
                new_centers.append(centers[i])
        centers = new_centers
    assignment = {}
    for r, c in cells:
        best, bd = 0, abs(r - centers[0][0]) + abs(c - centers[0][1])
        for i in range(1, n):
            d = abs(r - centers[i][0]) + abs(c - centers[i][1])
            if d < bd:
                bd, best = d, i
        assignment[(r, c)] = best
    order_stripes = sorted(range(n), key=lambda i: stripe_x[i])
    cluster_order = sorted(range(n), key=lambda i: centers[i][1])
    mapping = {ci: stripe_cols[order_stripes[k]] for k, ci in enumerate(cluster_order)}
    out = [[0] * w for _ in range(h)]
    for (r, c), i in assignment.items():
        out[r][c] = mapping[i]
    return out