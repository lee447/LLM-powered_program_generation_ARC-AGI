def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    pts = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c]!=0]
    min_r = min(r for r,c in pts)
    max_r = max(r for r,c in pts)
    min_c = min(c for r,c in pts)
    max_c = max(c for r,c in pts)
    shape = [row[min_c:max_c+1] for row in grid[min_r:max_r+1]]
    h = len(shape)
    w = len(shape[0])
    M = max(h,w)
    m = min(h,w)
    block_h = [M,m,M]
    block_w = [M,m,M]
    H = block_h[0]+block_h[1]+block_h[2]
    W = block_w[0]+block_w[1]+block_w[2]
    out = [[0]*W for _ in range(H)]
    def rot90cw(a):
        hh = len(a)
        ww = len(a[0])
        b = [[0]*hh for _ in range(ww)]
        for i in range(hh):
            for j in range(ww):
                b[j][hh-1-i] = a[i][j]
        return b
    def rot180(a):
        hh = len(a)
        ww = len(a[0])
        b = [[0]*ww for _ in range(hh)]
        for i in range(hh):
            for j in range(ww):
                b[hh-1-i][ww-1-j] = a[i][j]
        return b
    def rot90ccw(a):
        hh = len(a)
        ww = len(a[0])
        b = [[0]*hh for _ in range(ww)]
        for i in range(hh):
            for j in range(ww):
                b[ww-1-j][i] = a[i][j]
        return b
    rots = [
        (shape, (1,0)),
        (rot90cw(shape), (0,1)),
        (rot180(shape), (1,2)),
        (rot90ccw(shape), (2,1))
    ]
    for sh,(br,bc) in rots:
        off_r = sum(block_h[:br])
        off_c = sum(block_w[:bc])
        for i in range(len(sh)):
            for j in range(len(sh[0])):
                if sh[i][j]!=0:
                    out[off_r+i][off_c+j] = sh[i][j]
    return out