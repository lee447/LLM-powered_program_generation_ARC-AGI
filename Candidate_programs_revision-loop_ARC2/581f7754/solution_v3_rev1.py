from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    from collections import deque, defaultdict
    flat = [c for row in grid for c in row]
    bg = max(set(flat), key=flat.count)
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                q = deque([(i,j)])
                vis[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                rs = [x for x,_ in cells]
                cs = [y for _,y in cells]
                comps.append((col,cells,min(rs),max(rs),min(cs),max(cs)))
    axis = 1 if h>w else 0
    bycol = defaultdict(list)
    for comp in comps:
        bycol[comp[0]].append(comp)
    out = [[bg]*w for _ in range(h)]
    for col, group in bycol.items():
        if len(group)>1:
            centers = []
            for _,cells,r1,r2,c1,c2 in group:
                centers.append(((r1+r2)//2,(c1+c2)//2)[axis])
            centers.sort()
            tgt = centers[len(centers)//2]
            for _,cells,r1,r2,c1,c2 in group:
                ctr = ((r1+r2)//2,(c1+c2)//2)[axis]
                d = tgt-ctr
                for x,y in cells:
                    nx,ny = (x+d,y) if axis==0 else (x,y+d)
                    out[nx][ny] = grid[x][y]
        else:
            _,cells,_,_,_,_ = group[0]
            for x,y in cells:
                out[x][y] = grid[x][y]
    return out