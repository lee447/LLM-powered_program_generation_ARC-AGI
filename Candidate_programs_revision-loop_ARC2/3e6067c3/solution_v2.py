def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    B, BG = 1, 8
    pts = {}
    vis = [[False]*w for _ in range(h)]
    def dfs(r,c,color):
        stack=[(r,c)]; comp=[]
        while stack:
            x,y=stack.pop()
            if (0<=x<h and 0<=y<w and not vis[x][y] and grid[x][y]==color):
                vis[x][y]=True
                comp.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    stack.append((x+dx,y+dy))
        return comp
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c not in (B,BG) and not vis[i][j]:
                comp=dfs(i,j,c)
                if c not in pts: pts[c]=[]
                pts[c].append(comp)
    def center(comp):
        xs=[p[0] for p in comp]; ys=[p[1] for p in comp]
        return sum(xs)//len(xs), sum(ys)//len(ys)
    for color, comps in pts.items():
        if len(comps)!=2: continue
        (r1,c1),(r2,c2)=center(comps[0]), center(comps[1])
        if r1==r2:
            c0,c1_ = sorted((c1,c2))
            for y in range(c0, c1_+1):
                if out[r1][y] in (B,BG): out[r1][y]=color
        elif c1==c2:
            r0,r1_ = sorted((r1,r2))
            for x in range(r0, r1_+1):
                if out[x][c1] in (B,BG): out[x][c1]=color
    return out