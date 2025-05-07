def solve(grid):
    rmax, cmax = len(grid), len(grid[0])
    yrows = sorted({r for r in range(rmax) for c in range(cmax) if grid[r][c]==4})
    ycols = sorted({c for r in range(rmax) for c in range(cmax) if grid[r][c]==4})
    rects = []
    for i in range(len(yrows)):
        for j in range(i+1, len(yrows)):
            r1, r2 = yrows[i], yrows[j]
            for a in range(len(ycols)):
                for b in range(a+1, len(ycols)):
                    c1, c2 = ycols[a], ycols[b]
                    if grid[r1][c1]==4 and grid[r1][c2]==4 and grid[r2][c1]==4 and grid[r2][c2]==4:
                        if r2 - r1 > 1 and c2 - c1 > 1:
                            rects.append((r1, r2, c1, c2))
    reds = [(r, c) for r in range(rmax) for c in range(cmax) if grid[r][c]==2]
    orig = None
    for (r1, r2, c1, c2) in rects:
        for (r, c) in reds:
            if r1 < r < r2 and c1 < c < c2:
                orig = (r1, r2, c1, c2)
                break
        if orig:
            break
    if not orig:
        return grid
    r1o, r2o, c1o, c2o = orig
    shape = [(r - r1o, c - c1o) for (r, c) in reds]
    out = [row[:] for row in grid]
    for (r1, r2, c1, c2) in rects:
        if (r1, r2, c1, c2) == orig:
            continue
        for dr, dc in shape:
            rr, cc = r1 + dr, c1 + dc
            if 0 <= rr < rmax and 0 <= cc < cmax and out[rr][cc] == 0:
                out[rr][cc] = 2
    return out