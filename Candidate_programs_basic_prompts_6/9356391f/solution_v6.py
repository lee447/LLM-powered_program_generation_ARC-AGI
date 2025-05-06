def solve(grid):
    h,len_row = len(grid), len(grid[0])
    row0, row1 = grid[0], grid[1]
    segments = []
    j = 0
    while j < len_row:
        if row0[j] != 0:
            start = j
            while j+1 < len_row and row0[j+1] != 0:
                j += 1
            segments.append((start, j, j-start+1))
        j += 1
    a0,b0,_ = max(segments, key=lambda x: x[2])
    nonzeros = [i for i,v in enumerate(row0) if v != 0]
    a_seg, b_seg = min(nonzeros), max(nonzeros)
    seg = row0[a_seg:b_seg+1]
    rev = seg[::-1]
    target = row0[a0]
    centers = [(i,j) for i in range(h) for j in range(len_row) if grid[i][j]==target and not (i==0 and j==a0)]
    cr,cc = centers[0]
    half = b_seg - a_seg
    top, left = cr-half, cc-half
    size = 2*half + 1
    for o,v in enumerate(rev):
        if v==0: continue
        y0, y1 = left+o, left+size-1-o
        x0, x1 = top+o, top+size-1-o
        for y in range(y0, y1+1):
            grid[x0][y] = v
            grid[x1][y] = v
        for x in range(x0+1, x1):
            grid[x][y0] = v
            grid[x][y1] = v
    for j in range(len_row):
        if j < a0 or j > b0:
            if grid[0][j] != 0:
                grid[0][j] = row1[j]
    return grid