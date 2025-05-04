def solve(grid):
    h = len(grid)
    w = len(grid[0])
    anchors = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v in (1,2,3,6):
                anchors.setdefault(v, []).append((r,c))
    offs = {1:(-1,2),2:(0,-4),3:(3,0),6:(-6,0)}
    out = [[0]*w for _ in range(h)]
    overlaps = []
    for col, pts in anchors.items():
        if len(pts)==2:
            p1,p2 = pts
        else:
            r,c = pts[0]
            dy,dx = offs[col]
            p1 = (r,c)
            p2 = (r+dy,c+dx)
        (r0,c0),(r1,c1) = p1,p2
        dr = 0 if r1==r0 else (1 if r1>r0 else -1)
        dc = 0 if c1==c0 else (1 if c1>c0 else -1)
        cc = c0
        while cc!=c1:
            cc += dc
            if out[r0][cc]==5:
                out[r0][cc]=4
                overlaps.append((r0,cc))
            elif out[r0][cc]==0:
                out[r0][cc]=5
        rr = r0
        while rr!=r1:
            rr += dr
            if out[rr][c1]==5:
                out[rr][c1]=4
                overlaps.append((rr,c1))
            elif out[rr][c1]==0:
                out[rr][c1]=5
        out[r0][c0] = col
        out[r1][c1] = col
    for r,c in overlaps:
        rr,cc = r+1,c-1
        while 0<=rr<h and 0<=cc<w and out[rr][cc]==0:
            out[rr][cc]=4
            rr+=1; cc-=1
    return out