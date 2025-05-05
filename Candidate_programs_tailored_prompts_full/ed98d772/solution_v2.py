def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[[0]*(w*2) for _ in range(h*2)]
    pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]!=0]
    if not pts: return out
    v=grid[pts[0][0]][pts[0][1]]
    def r90(p):return(p[1],h-1-p[0])
    def r180(p):return(h-1-p[0],w-1-p[1])
    def r270(p):return(w-1-p[1],p[0])
    for r,c in pts: out[r][c]=v
    for r,c in pts:
        nr,nc=r270((r,c)); out[nr][nc+w]=v
    for r,c in pts:
        nr,nc=r180((r,c)); out[nr+h][nc]=v
    for r,c in pts:
        nr,nc=r90((r,c)); out[nr+h][nc+w]=v
    return out