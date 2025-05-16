from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    color_positions = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                color_positions.setdefault(v, []).append((r, c))
    clusters = []
    for v, pts in color_positions.items():
        rs = [p[0] for p in pts]
        cs = [p[1] for p in pts]
        rmin, rmax = min(rs), max(rs)
        cmin, cmax = min(cs), max(cs)
        if rmax - rmin == 2 and cmax - cmin == 2:
            center = ((rmin + rmax) // 2, (cmin + cmax) // 2)
            clusters.append((v, pts, center))
    new = [row[:] for row in grid]
    for v, pts, _ in clusters:
        for r, c in pts:
            new[r][c] = 0
    for v, pts, (cr, cc) in clusters:
        count = len(pts)
        if count == 9:
            arms = [(-1,0),(1,0),(0,-1),(0,1)]
        else:
            arms = [(0,-1),(0,1)]
        for dr, dc in arms:
            r2, c2 = cr+dr, cc+dc
            if 0 <= r2 < H and 0 <= c2 < W and new[r2][c2] == 0:
                new[r2][c2] = v
        if count == 9:
            mr, mc = H-1-cr, W-1-cc
            for dr, dc in arms:
                r2, c2 = mr+dr, mc+dc
                if 0 <= r2 < H and 0 <= c2 < W and new[r2][c2] == 0:
                    new[r2][c2] = v
    return new