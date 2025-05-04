def solve(grid):
    h,len_row= len(grid), len(grid[0])
    tpl=[]
    rs=[r for r in range(h) for c in range(len_row) if grid[r][c] not in (0,1)]
    if rs:
        cs=[c for r in range(h) for c in range(len_row) if grid[r][c] not in (0,1)]
        mr,Mr=min(rs),max(rs)
        mc,Mc=min(cs),max(cs)
        for r in range(mr,Mr+1):
            for c in range(mc,Mc+1):
                v=grid[r][c]
                if v not in (0,1): tpl.append((r-mr,c-mc,v))
    vis=[[False]*len_row for _ in range(h)]
    origins=[]
    for i in range(h):
        for j in range(len_row):
            if grid[i][j]==1 and not vis[i][j]:
                stack=[(i,j)]
                minr,minc=i,j
                while stack:
                    r,c=stack.pop()
                    if vis[r][c]: continue
                    vis[r][c]=True
                    minr,minc=min(minr,r),min(minc,c)
                    for dr in(-1,0,1):
                        for dc in(-1,0,1):
                            nr, nc = r+dr, c+dc
                            if 0<=nr<h and 0<=nc<len_row and not vis[nr][nc] and grid[nr][nc]==1:
                                stack.append((nr,nc))
                origins.append((minr,minc))
    out=[row[:] for row in grid]
    for r in range(h):
        for c in range(len_row):
            if grid[r][c]==1: out[r][c]=0
    for r0,c0 in origins:
        for dr,dc,v in tpl:
            out[r0+dr][c0+dc]=v
    return out