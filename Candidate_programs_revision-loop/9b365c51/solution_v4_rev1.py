from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe_x = [c for c, v in enumerate(grid[0]) if v != 0]
    stripe_x.sort()
    stripe_cols = [grid[0][c] for c in stripe_x]
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    if not cells:
        return [[0] * w for _ in range(h)]
    xs = sorted({c for _, c in cells})
    m, n = len(xs), len(stripe_cols)
    min_c, max_c = xs[0], xs[-1]
    centers = [min_c + (max_c - min_c) * i / (n - 1) if n > 1 else min_c for i in range(n)]
    for _ in range(10):
        clusters = [[] for _ in range(n)]
        for c in xs:
            idx = min(range(n), key=lambda i: (abs(c - centers[i]), i))
            clusters[idx].append(c)
        new_centers = []
        for i in range(n):
            if clusters[i]:
                new_centers.append(sum(clusters[i]) / len(clusters[i]))
            else:
                new_centers.append(centers[i])
        centers = new_centers
    idx_map = {}
    for c in xs:
        idx_map[c] = min(range(n), key=lambda i: (abs(c - centers[i]), i))
    out = [[0] * w for _ in range(h)]
    for r, c in cells:
        out[r][c] = stripe_cols[idx_map[c]]
    return out