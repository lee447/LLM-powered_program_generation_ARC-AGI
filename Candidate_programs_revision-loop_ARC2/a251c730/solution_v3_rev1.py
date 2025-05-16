from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    bounds = {}
    for r in range(H):
        for c, v in enumerate(grid[r]):
            if v not in bounds:
                bounds[v] = [r, r, c, c]
            else:
                b = bounds[v]
                if r < b[0]: b[0] = r
                if r > b[1]: b[1] = r
                if c < b[2]: b[2] = c
                if c > b[3]: b[3] = c
    frames = []
    for v, (rmin, rmax, cmin, cmax) in bounds.items():
        if rmax - rmin < 2 or cmax - cmin < 2:
            continue
        ok = True
        for c in range(cmin, cmax + 1):
            if grid[rmin][c] != v or grid[rmax][c] != v:
                ok = False
                break
        if not ok:
            continue
        for r in range(rmin, rmax + 1):
            if grid[r][cmin] != v or grid[r][cmax] != v:
                ok = False
                break
        if ok:
            frames.append((v, rmin, rmax, cmin, cmax))
    if not frames:
        return grid
    v, rmin, rmax, cmin, cmax = min(frames, key=lambda x: (x[2]-x[1]+1)*(x[4]-x[3]+1))
    interior = [row[cmin+1:cmax] for row in grid[rmin+1:rmax]]
    h = len(interior)
    w = len(interior[0]) if h else 0
    res = [[v] * (w + 2) for _ in range(h + 2)]
    for i in range(h):
        for j in range(w):
            res[i+1][j+1] = interior[i][j]
    return res