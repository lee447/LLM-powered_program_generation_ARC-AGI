def solve(grid):
    h,len0=len(grid),len(grid[0])
    out=[row[:] for row in grid]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    while True:
        vis=[[False]*len0 for _ in range(h)]
        filled=False
        for i in range(h):
            for j in range(len0):
                if out[i][j]==0 and not vis[i][j]:
                    stack=[(i,j)]
                    comp=[]
                    touch_border=False
                    vis[i][j]=True
                    while stack:
                        r,c=stack.pop()
                        comp.append((r,c))
                        if r==0 or r==h-1 or c==0 or c==len0-1:
                            touch_border=True
                        for dr,dc in dirs:
                            nr,nc=r+dr,c+dc
                            if 0<=nr<h and 0<=nc<len0 and not vis[nr][nc] and out[nr][nc]==0:
                                vis[nr][nc]=True
                                stack.append((nr,nc))
                    if not touch_border:
                        neigh=set()
                        for r,c in comp:
                            for dr,dc in dirs:
                                nr,nc=r+dr,c+dc
                                if 0<=nr<h and 0<=nc<len0 and out[nr][nc]!=0:
                                    neigh.add(out[nr][nc])
                        if len(neigh)==1:
                            c0=neigh.pop()
                            fill=c0+1
                            for r,c in comp:
                                out[r][c]=fill
                            filled=True
        if not filled:
            break
    return out