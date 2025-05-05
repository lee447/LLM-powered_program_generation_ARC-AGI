from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    from collections import defaultdict
    clusters = defaultdict(list)
    for r in range(R-1):
        for c in range(C-1):
            v = grid[r][c]
            if v == grid[r][c+1] == grid[r+1][c] == grid[r+1][c+1]:
                clusters[v].append((r, c))
    if not clusters:
        return []
    items = sorted(clusters.items(), key=lambda kv: len(kv[1]))
    cluster_color = items[0][0]
    stripe_color = items[-1][0] if len(items) > 1 else items[0][0]
    cr, cc = clusters[cluster_color][0]
    cr0, cr1 = cr, cr + 1
    cc0, cc1 = cc, cc + 1
    stripe_cells = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == stripe_color]
    rs = [r for r, _ in stripe_cells]
    cs = [c for _, c in stripe_cells]
    sr0, sr1 = min(rs), max(rs)
    sc0, sc1 = min(cs), max(cs)
    if cr1 < sr0:
        r0, r1 = cr1 + 1, sr0 - 1
    else:
        r0, r1 = sr1 + 1, cr0 - 1
    if cc1 < sc0:
        c0, c1 = cc1 + 1, sc0 - 1
    else:
        c0, c1 = sc1 + 1, cc0 - 1
    return [row[c0:c1+1] for row in grid[r0:r1+1]]