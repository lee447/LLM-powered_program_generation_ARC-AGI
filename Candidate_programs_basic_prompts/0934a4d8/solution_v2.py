def solve(grid):
    R, C = len(grid), len(grid[0])
    # find the solid rectangle color (maximal area, perfect fill)
    best = None
    for val in set(v for row in grid for v in row):
        pts = [(i,j) for i in range(R) for j in range(C) if grid[i][j]==val]
        if not pts: continue
        rs = [i for i,_ in pts]; cs = [j for _,j in pts]
        r0,r1,minr = min(rs),max(rs),None
        c0,c1 = min(cs),max(cs)
        h,w = r1-r0+1, c1-c0+1
        if len(pts)==h*w:
            best = (val, r0, r1, c0, c1)
            break
    if best is None:
        return []
    _, r0, r1, c0, c1 = best
    H, W = r1-r0+1, c1-c0+1
    out = [[0]*W for _ in range(H)]
    # mirror horizontally the block immediately to the left of the solid rectangle
    for i in range(H):
        for j in range(W):
            out[i][j] = grid[r0+i][c0-1-j]
    return out