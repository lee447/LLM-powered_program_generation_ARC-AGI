from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = grid
    out = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if orig[i][j]==1 and not vis[i][j]:
                stk = [(i,j)]
                vis[i][j]=True
                comp=[]
                while stk:
                    r,c=stk.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and orig[nr][nc]==1:
                            vis[nr][nc]=True
                            stk.append((nr,nc))
                comps.append(comp)
    rects=[]
    for comp in comps:
        rs=[r for r,_ in comp]; cs=[c for _,c in comp]
        r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
        area = (r1-r0+1)*(maxc-minc+1)
        if len(comp)==area or len(comp)==2*(r1-r0+1)+2*(maxc-minc+1)-4:
            rects.append((r0,r1,minc,maxc))
    for r0,r1,c0,c1 in rects:
        for c in range(c0-1,c1+2):
            if 0<=c<w:
                if 0<=r0-1<h: out[r0-1][c]=2
                if 0<=r1+1<h: out[r1+1][c]=2
        for r in range(r0-1,r1+2):
            if 0<=r<h:
                if 0<=c0-1<w: out[r][c0-1]=2
                if 0<=c1+1<w: out[r][c1+1]=2
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):
                if orig[r][c]!=1:
                    if (r-r0)*(c1-c0) <= (r1-r0)*(c-c0):
                        out[r][c]=8
                    else:
                        out[r][c]=6
    return out