def solve(grid):
    H, W = len(grid), len(grid[0])
    bounds = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                if v not in bounds:
                    bounds[v] = [r, c, r, c]
                else:
                    br = bounds[v]
                    if r < br[0]: br[0] = r
                    if c < br[1]: br[1] = c
                    if r > br[2]: br[2] = r
                    if c > br[3]: br[3] = c
    res = [row[:] for row in grid]
    for v, (minr, minc, maxr, maxc) in bounds.items():
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                if res[r][c] == 0:
                    res[r][c] = v
    return res