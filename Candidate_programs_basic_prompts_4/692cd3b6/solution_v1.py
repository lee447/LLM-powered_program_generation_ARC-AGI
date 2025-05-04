def solve(grid):
    h = len(grid)
    w = len(grid[0])
    holes = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 5:
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    rr, cc = r+dr, c+dc
                    if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
                        holes.append((rr,cc))
                        break
    if len(holes) != 2:
        return grid
    (r0,c0),(r1,c1) = holes
    rmin, rmax = min(r0,r1), max(r0,r1)
    cmin, cmax = min(c0,c1), max(c0,c1)
    out = [row[:] for row in grid]
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if out[r][c] == 0:
                out[r][c] = 4
    return out