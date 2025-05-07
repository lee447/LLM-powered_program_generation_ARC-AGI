from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    best: Tuple[int,int,int,int,int] = None
    for c in range(1,10):
        pts = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==c]
        if not pts: continue
        ys = [i for i,j in pts]; xs = [j for i,j in pts]
        y0,y1 = min(ys), max(ys); x0,x1 = min(xs), max(xs)
        if y1-y0<1 or x1-x0<1: continue
        ok = True
        for i in (y0, y1):
            for j in range(x0, x1+1):
                if grid[i][j]!=c: ok=False
        for i in range(y0, y1+1):
            for j in (x0, x1):
                if grid[i][j]!=c: ok=False
        if ok:
            area = (y1-y0+1)*(x1-x0+1)
            if best is None or area > (best[1]-best[0]+1)*(best[3]-best[2]+1):
                best = (y0,y1,x0,x1,c)
    if best is None:
        # find largest all-nonzero rectangle
        best_rect = None
        for y0 in range(h):
            for x0 in range(w):
                if grid[y0][x0]==0: continue
                for y1 in range(y0+1, h):
                    for x1 in range(x0+1, w):
                        area = (y1-y0+1)*(x1-x0+1)
                        if best_rect and area <= (best_rect[1]-best_rect[0]+1)*(best_rect[3]-best_rect[2]+1):
                            continue
                        ok = True
                        for i in range(y0, y1+1):
                            for j in range(x0, x1+1):
                                if grid[i][j]==0:
                                    ok=False; break
                            if not ok: break
                        if ok:
                            best_rect = (y0,y1,x0,x1)
        if best_rect is None:
            return grid
        y0,y1,x0,x1 = best_rect
        sub = [row[x0:x1+1] for row in grid[y0:y1+1]]
        vals = sorted({v for row in sub for v in row if v>0})
        m = {v:i+1 for i,v in enumerate(vals)}
        return [[m.get(v,0) for v in row] for row in sub]
    y0,y1,x0,x1,c = best
    sub = [row[x0:x1+1] for row in grid[y0:y1+1]]
    ih, iw = len(sub), len(sub[0])
    inner = []
    vals = [sub[i][j] for i in range(1,ih-1) for j in range(1,iw-1) if sub[i][j]!=c]
    mx = max(vals) if vals else 0
    for i in range(ih):
        row = []
        for j in range(iw):
            v = sub[i][j]
            if i in (0,ih-1) or j in (0,iw-1):
                row.append(v)
            else:
                if v==c:
                    row.append(v)
                else:
                    row.append(mx - v + 1)
        inner.append(row)
    return inner