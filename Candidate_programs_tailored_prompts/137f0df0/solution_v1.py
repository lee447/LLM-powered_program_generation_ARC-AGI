def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    clusters = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5 and grid[r+1][c+1]==5:
                clusters.append((r,c))
    rs = sorted({r for r,c in clusters})
    cs = sorted({c for r,c in clusters})
    for r,c in clusters:
        res[r][c]=5; res[r][c+1]=5; res[r+1][c]=5; res[r+1][c+1]=5
    row_start, row_end = rs[0], rs[-1]+2
    col_start, col_end = cs[0], cs[-1]+2
    dr_gaps = [(rs[i]+2, rs[i+1]) for i in range(len(rs)-1) if rs[i+1] > rs[i]+2]
    dc_gaps = [(cs[j]+2, cs[j+1]) for j in range(len(cs)-1) if cs[j+1] > cs[j]+2]
    for r0, r1 in dr_gaps:
        for r in range(r0, r1):
            for c in range(col_start, col_end):
                if res[r][c]==0:
                    res[r][c]=2
    for c0, c1 in dc_gaps:
        for c in range(c0, c1):
            for r in range(row_start, row_end):
                if res[r][c]==0:
                    res[r][c]=2
    # horizontal stripe caps
    left_w = col_start
    right_w = w - col_end
    for r0, r1 in dr_gaps:
        if left_w>0:
            for r in range(r0, r1):
                for c in range(0, col_start):
                    if res[r][c]==0:
                        res[r][c]=1
        if right_w>0:
            for r in range(r0, r1):
                for c in range(col_end, w):
                    if res[r][c]==0:
                        res[r][c]=1
    # vertical stripe caps
    top_h = row_start
    bottom_h = h - row_end
    for c0, c1 in dc_gaps:
        if top_h>0:
            for r in range(0, row_start):
                for c in range(c0, c1):
                    if res[r][c]==0:
                        res[r][c]=1
        if bottom_h>0:
            for r in range(row_end, h):
                for c in range(c0, c1):
                    if res[r][c]==0:
                        res[r][c]=1
    return res