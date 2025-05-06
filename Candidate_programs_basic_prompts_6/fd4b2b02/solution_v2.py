def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    if not pts:
        return [[0]*W for _ in range(H)]
    A = grid[pts[0][0]][pts[0][1]]
    minr = min(r for r,c in pts)
    maxr = max(r for r,c in pts)
    minc = min(c for r,c in pts)
    maxc = max(c for r,c in pts)
    h = maxr - minr + 1
    w = maxc - minc + 1
    shape = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
    def rot(sh):
        hh, ww = len(sh), len(sh[0])
        return [[sh[hh-1-j][i] for j in range(hh)] for i in range(ww)]
    B = 3 if A == 6 else 6
    cy = (H-1)/2
    cx = (W-1)/2
    sy = (minr+maxr)/2
    sx = (minc+maxc)/2
    dr0 = sy - cy
    dc0 = sx - cx
    res = [[0]*W for _ in range(H)]
    for k in range(4):
        if k == 0:
            dr_k, dc_k = dr0, dc0
        elif k == 1:
            dr_k, dc_k = -dc0, dr0
        elif k == 2:
            dr_k, dc_k = -dr0, -dc0
        else:
            dr_k, dc_k = dc0, -dr0
        sh = shape if k%2==0 else rot(shape)
        col = A if k%2==0 else B
        for f in range(1, max(H, W)):
            cy2 = cy + dr_k * f
            cx2 = cx + dc_k * f
            top = int(round(cy2 - (len(sh)-1)/2))
            left = int(round(cx2 - (len(sh[0])-1)/2))
            if top < 0 or left < 0 or top+len(sh) > H or left+len(sh[0]) > W:
                break
            for i in range(len(sh)):
                for j in range(len(sh[0])):
                    if sh[i][j] != 0:
                        res[top+i][left+j] = col
    return res