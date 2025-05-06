def solve(grid):
    h,len_row = len(grid), len(grid[0])
    vis = [[False]*len_row for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(len_row):
            if grid[i][j]!=0 and not vis[i][j]:
                stack=[(i,j)]
                vis[i][j]=True
                pts=[]
                while stack:
                    y,x=stack.pop()
                    pts.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<len_row and grid[ny][nx]!=0 and not vis[ny][nx]:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
                miny,maxy,minx,maxx = min(ys), max(ys), min(xs), max(xs)
                mat = [[0]*(maxx-minx+1) for _ in range(maxy-miny+1)]
                for y,x in pts:
                    mat[y-miny][x-minx] = grid[y][x]
                comps.append({
                    "miny":miny, "maxy":maxy,
                    "minx":minx, "maxx":maxx,
                    "w":maxx-minx+1, "h":maxy-miny+1,
                    "mat":mat, "x":None
                })
    W = len_row
    for r in range(h):
        group = [c for c in comps if c["miny"]<=r<=c["maxy"]]
        if len(group)>1:
            group.sort(key=lambda c:c["minx"])
            total = sum(c["w"] for c in group)
            left = W - total
            cur = left
            for c in group:
                if c["x"] is None:
                    c["x"] = cur
                cur += c["w"]
    for c in comps:
        if c["x"] is None:
            c["x"] = W - c["w"]
    out = [[0]*W for _ in range(h)]
    for c in comps:
        for dy in range(c["h"]):
            for dx in range(c["w"]):
                v = c["mat"][dy][dx]
                if v!=0:
                    out[c["miny"]+dy][c["x"]+dx] = v
    return out