from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    B, BG = 1, 8
    vis = [[False]*w for _ in range(h)]
    comps = {}
    def dfs(r,c,color):
        stack=[(r,c)]; comp=[]
        while stack:
            x,y=stack.pop()
            if 0<=x<h and 0<=y<w and not vis[x][y] and grid[x][y]==color:
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
                comps.setdefault(c,[]).append(comp)
    for color, clist in comps.items():
        if len(clist)!=2: continue
        c1, c2 = clist
        xs1 = [p[0] for p in c1]; ys1 = [p[1] for p in c1]
        xs2 = [p[0] for p in c2]; ys2 = [p[1] for p in c2]
        r1c, r1 = sum(xs1)//len(xs1), None
        c1c = sum(ys1)//len(ys1)
        r2c = sum(xs2)//len(xs2)
        c2c = sum(ys2)//len(ys2)
        x1min, x1max, y1min, y1max = min(xs1), max(xs1), min(ys1), max(ys1)
        x2min, x2max, y2min, y2max = min(xs2), max(xs2), min(ys2), max(ys2)
        if r1c == r2c:
            y0,y1 = sorted((y1min,y2min))
            for y in range(y0,y1+1):
                if out[r1c][y] in (B,BG): out[r1c][y]=color
        elif c1c == c2c:
            x0,x1 = sorted((x1min,x2min))
            for x in range(x0,x1+1):
                if out[x][c1c] in (B,BG): out[x][c1c]=color
        else:
            # vertical segment at comp1's cols
            for x in range(min(r1c,r2c), max(r1c,r2c)+1):
                for y in range(y1min,y1max+1):
                    if out[x][y] in (B,BG): out[x][y]=color
            # horizontal segment at comp2's rows
            for y in range(min(c1c,c2c), max(c1c,c2c)+1):
                for x in range(x2min,x2max+1):
                    if out[x][y] in (B,BG): out[x][y]=color
    return out