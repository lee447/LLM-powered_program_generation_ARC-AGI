def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    opens = []
    for r, c in centers:
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr, cc = r+dr, c+dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
                opens.append((rr, cc))
                break
    (r1, c1), (r2, c2) = opens
    rmin, rmax = min(r1, r2), max(r1, r2)
    cmin, cmax = min(c1, c2), max(c1, c2)
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if grid[r][c] == 0:
                grid[r][c] = 4
    return grid