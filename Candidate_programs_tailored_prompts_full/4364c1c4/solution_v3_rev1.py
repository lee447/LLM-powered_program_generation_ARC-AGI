import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = max(set(flat), key=flat.count)
    vis = [[False]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                pts = []
                dq = [(i,j)]
                vis[i][j] = True
                while dq:
                    r,c = dq.pop()
                    pts.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==col:
                            vis[nr][nc] = True
                            dq.append((nr,nc))
                minr = min(r for r,c in pts)
                minc = min(c for r,c in pts)
                comps.append((minr, minc, pts, col))
    comps.sort(key=lambda x:(x[0],x[1]))
    out = [[bg]*w for _ in range(h)]
    for idx, (_,_,pts,col) in enumerate(comps):
        dx = -1 if idx%2==0 else 1
        for r,c in pts:
            out[r][c+dx] = col
    return out