def solve(grid):
    n, m = len(grid), len(grid[0])
    # find the marker color (8) and its bounding box
    mark = max(c for row in grid for c in row if c != 0 and sum(1 for r in grid for v in r if v == c) < n*m)
    r0 = min(i for i,row in enumerate(grid) for j,v in enumerate(row) if v==mark)
    r1 = max(i for i,row in enumerate(grid) for j,v in enumerate(row) if v==mark)
    c0 = min(j for row in grid for j,v in enumerate(row) if v==mark)
    c1 = max(j for row in grid for j,v in enumerate(row) if v==mark)
    h, w = r1-r0+1, c1-c0+1
    out = [[0]*w for _ in range(h)]
    # fill out[i][j] by looking symmetrically around the marker block
    for i in range(h):
        for j in range(w):
            vals = []
            # north
            if r0-1-i>=0: vals.append(grid[r0-1-i][c0+j])
            # west
            if c0-1-j>=0: vals.append(grid[r0+i][c0-1-j])
            # south
            if r1+1+i<n: vals.append(grid[r1+1+i][c1-j])
            # east
            if c1+1+j<m: vals.append(grid[r1-i][c1+1+j])
            # choose most frequent if any
            if vals:
                out[i][j] = max(set(vals), key=vals.count)
    return out