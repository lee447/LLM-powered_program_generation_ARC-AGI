from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    shape_pts = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                start = (i,j); break
        else:
            continue
        break
    q = [start]; seen[start[0]][start[1]] = True
    while q:
        y,x = q.pop()
        shape_pts.append((y,x))
        for dy,dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]!=0:
                seen[ny][nx] = True
                q.append((ny,nx))
    ys = [y for y,_ in shape_pts]; xs = [x for _,x in shape_pts]
    y1, y2 = min(ys), max(ys); x1, x2 = min(xs), max(xs)
    sh, sw = y2-y1+1, x2-x1+1
    shape = [row[x1:x2+1] for row in grid[y1:y2+1]]
    seeds = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not (y1<=i<=y2 and x1<=j<=x2):
                seeds.append((i,j,grid[i][j]))
    groups = {'E':[], 'S':[]}
    for i,j,v in seeds:
        if x1<=j<=x2 and i>y2: groups['S'].append((i,j,v))
        if y1<=i<=y2 and j>x2: groups['E'].append((i,j,v))
    out = [row[:] for row in grid]
    def place(dir, group):
        if not group: return
        if dir=='E':
            ry, rx = y1, x2+1
        else:
            ry, rx = y2+1, x1
        sv = sorted(set([v for _,_,v in group]))
        pv = sorted(set([c for row in shape for c in row]))
        import itertools
        def inv_t(ty, tx, t):
            if t==0: return ty, tx
            if t==1: return ty, sw-1-tx
            if t==2: return sh-1-ty, tx
            if t==3: return sh-1-ty, sw-1-tx
        for t in range(4):
            for perm in itertools.permutations(sv, len(pv)):
                mp = {pv[i]: perm[i] for i in range(len(pv))}
                ok = True
                for yi, xi, vv in group:
                    ty, tx = yi-ry, xi-rx
                    oy, ox = inv_t(ty, tx, t)
                    if mp.get(shape[oy][ox],None) != vv:
                        ok = False; break
                if not ok: continue
                for yi2 in range(sh):
                    for xi2 in range(sw):
                        oy, ox = inv_t(yi2, xi2, t)
                        out[ry+yi2][rx+xi2] = mp.get(shape[oy][ox], out[ry+yi2][rx+xi2])
                return
    place('E', groups['E'])
    place('S', groups['S'])
    return out