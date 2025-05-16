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
        rs = [r for r, _ in pts]
        cs = [c for _, c in pts]
        rmin, rmax = min(rs), max(rs)
        cmin, cmax = min(cs), max(cs)
        if rmax - rmin == 2 and cmax - cmin == 2 and len(pts) == 9:
            clusters.append((v, rmin, rmax, cmin, cmax, (rmin + 1, cmin + 1)))
    new = [row[:] for row in grid]
    for v, rmin, rmax, cmin, cmax, _ in clusters:
        for r in range(rmin, rmax + 1):
            for c in range(cmin, cmax + 1):
                new[r][c] = 0
    for v, _, _, _, _, (cr, cc) in clusters:
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r2, c2 = cr + dr, cc + dc
            if 0 <= r2 < H and 0 <= c2 < W and new[r2][c2] == 0:
                new[r2][c2] = v
    return new