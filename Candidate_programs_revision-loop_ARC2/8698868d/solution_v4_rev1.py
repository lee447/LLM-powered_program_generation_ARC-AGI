from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    vis = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if not vis[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<R and 0<=ny<C and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                xs = [x for x,_ in cells]; ys = [y for _,y in cells]
                comps.append((col, min(xs), max(xs), min(ys), max(ys), cells))
    cnt = {}
    for row in grid:
        for v in row:
            cnt[v] = cnt.get(v,0)+1
    bg = max(cnt, key=lambda k: cnt[k])
    sizes = []
    for col,x0,x1,y0,y1,cells in comps:
        h, w = x1-x0+1, y1-y0+1
        if col!=bg and h==w and h>2:
            sizes.append(h)
    if not sizes:
        return grid
    D = max(sizes)
    d = D-2
    frames = [c for c in comps if c[0]!=bg and (c[2]-c[1]+1)==D and (c[4]-c[3]+1)==D]
    smalls = [c for c in comps if c[0]!=bg and (c[2]-c[1]+1)==d and (c[4]-c[3]+1)==d]
    frames = sorted(frames, key=lambda c:(c[1],c[3]))
    smalls = sorted(smalls, key=lambda c:(c[1],c[3]))
    mapping = { (f[1],f[3]):s for f,s in zip(frames, smalls) }
    mats = {}
    for col,x0,x1,y0,y1,cells in frames:
        mat = [[col]*D for _ in range(D)]
        sx,_,sy,_,_=mapping[(x0,y0)]
        pat = [[grid[i][j] for j in range(sy,sy+d)] for i in range(sx,sx+d)]
        for i in range(d):
            for j in range(d):
                v = pat[i][j]
                mat[i+1][j+1] = v if v!=bg else col
        mats[(x0,y0)] = mat
    out = []
    rows = sorted(set(f[1] for f in frames))
    for rx in rows:
        row_frames = [f for f in frames if f[1]==rx]
        row_frames.sort(key=lambda f:f[3])
        for i in range(D):
            row = []
            for _,_,_,y0,_,_ in row_frames:
                row += mats[(rx,y0)][i]
            out.append(row)
    return out