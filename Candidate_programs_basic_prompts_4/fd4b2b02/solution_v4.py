def solve(grid):
    H=len(grid); W=len(grid[0])
    pts=[(y,x) for y in range(H) for x in range(W) if grid[y][x]!=0]
    if not pts: return grid
    origColor=grid[pts[0][0]][pts[0][1]]
    otherColor=3 if origColor==6 else 6
    ys=[y for y,x in pts]; xs=[x for y,x in pts]
    y0,y1=min(ys),max(ys); x0,x1=min(xs),max(xs)
    h=y1-y0+1; w=x1-x0+1
    shape=[[(y0+i,x0+j) in pts for j in range(w)] for i in range(h)]
    rot=[[shape[h-1-j][i] for j in range(h)] for i in range(w)]
    D=h+w
    out=[[0]*W for _ in range(H)]
    for ky in range(-W//D-2, H//D+3):
        for kx in range(-W//D-2, W//D+3):
            oy=y0+ky*D; ox=x0+kx*D
            for i in range(h):
                for j in range(w):
                    if shape[i][j]:
                        yy=oy+i; xx=ox+j
                        if 0<=yy<H and 0<=xx<W:
                            out[yy][xx]=origColor
            ry=y0+ky*D - w; rx=x0+kx*D + w
            ok=True
            for i in range(w):
                for j in range(h):
                    if rot[i][j]:
                        yy=ry+i; xx=rx+j
                        if not (0<=yy<H and 0<=xx<W):
                            ok=False; break
                if not ok: break
            if ok:
                for i in range(w):
                    for j in range(h):
                        if rot[i][j]:
                            out[ry+i][rx+j]=otherColor
    return out