def solve(grid):
    h, w = len(grid), len(grid[0])
    ys = sorted({y for y in range(h) for x in range(w) if grid[y][x]==6})
    top, mid, bot = ys[0], ys[1], ys[2]
    out = [row[:] for row in grid]
    def clusters(y):
        segs = []
        cur = []
        for x in range(w):
            if grid[y][x]==6:
                cur.append(x)
            else:
                if cur:
                    segs.append(cur)
                    cur=[]
        if cur: segs.append(cur)
        return segs
    for y, role in ((top,0),(mid,1),(bot,2)):
        for seg in clusters(y):
            m = len(seg)
            for j,x in enumerate(seg):
                if role==0:
                    out[y][x] = 1 if j==0 else 7
                elif role==1:
                    out[y][x] = 9 if j==m-1 else 7
                else:
                    out[y][x] = 7 if j==0 else 9
    return out