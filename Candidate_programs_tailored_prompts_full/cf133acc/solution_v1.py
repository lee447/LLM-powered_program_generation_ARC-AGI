def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    counts = [(sum(1 for r in range(h) if grid[r][j] != 0), j) for j in range(w)]
    cols = [j for _, j in sorted(counts, reverse=True)[:2]]
    j0, j1 = sorted(cols)
    for i in range(h):
        for j in (j0, j1):
            if out[i][j] == 0:
                if j > 0 and out[i][j-1] != 0:
                    out[i][j] = out[i][j-1]
                elif j < w-1 and out[i][j+1] != 0:
                    out[i][j] = out[i][j+1]
    bars = [i for i in range(h) if any((grid[i][j0] == 0 and ((j0>0 and grid[i][j0-1]!=0) or (j0<w-1 and grid[i][j0+1]!=0))) or
                                      (grid[i][j1] == 0 and ((j1>0 and grid[i][j1-1]!=0) or (j1<w-1 and grid[i][j1+1]!=0))) for j in (j0, j1))]
    last = max(bars) if bars else -1
    for j in (j0, j1):
        filled = [i for i in range(last+1) if out[i][j] != 0]
        for r in range(last+1):
            if out[r][j] == 0:
                m = min(i for i in filled if i > r)
                out[r][j] = out[m][j]
    return out