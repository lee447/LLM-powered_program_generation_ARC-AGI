from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    color_cc = {}
    for r in range(h):
        for c in range(w):
            col = grid[r][c]
            if col != 0 and not seen[r][c]:
                stack = [(r,c)]
                seen[r][c] = True
                comp = []
                while stack:
                    y,x = stack.pop()
                    comp.append((y,x))
                    for dy,dx in dirs:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == col:
                            seen[ny][nx] = True
                            stack.append((ny,nx))
                color_cc.setdefault(col, []).append(comp)
    # build segments
    color_segs = {}
    color_minx = {}
    color_maxrun = {}
    for col, ccs in color_cc.items():
        minx = w
        maxrun = 0
        comps = []
        for comp in ccs:
            byrow = {}
            for y,x in comp:
                minx = min(minx, x)
                byrow.setdefault(y, []).append(x)
            rows = sorted(byrow)
            segs = []
            for r in rows:
                xs = sorted(byrow[r])
                i0 = xs[0]
                cnt = 1
                for i in range(1, len(xs)):
                    if xs[i] == xs[i-1] + 1:
                        cnt += 1
                    else:
                        segs.append(cnt)
                        maxrun = max(maxrun, cnt)
                        i0 = xs[i]
                        cnt = 1
                segs.append(cnt)
                maxrun = max(maxrun, cnt)
            comps.append((comp, segs))
        color_segs[col] = comps
        color_minx[col] = minx
        color_maxrun[col] = maxrun
    # order colors by minx
    cols = sorted(color_cc.keys(), key=lambda c: color_minx[c])
    # compute x offsets
    offsets = {}
    cur = 0
    for c in cols:
        offsets[c] = cur
        cur += color_maxrun[c] + 2
    out = [[0]*w for _ in range(h)]
    for c in cols:
        comps = color_segs[c]
        # sort CCs by size desc then by min row asc then min col asc
        def keyfn(item):
            comp, segs = item
            size = len(comp)
            minr = min(y for y,x in comp)
            minc = min(x for y,x in comp)
            return (-size, minr, minc)
        comps_sorted = sorted(comps, key=keyfn)
        yptr = h
        xoff = offsets[c]
        for comp, segs in comps_sorted:
            cnt = len(segs)
            yptr -= cnt
            for i, ln in enumerate(segs):
                r = yptr + i
                for cc in range(ln):
                    if 0 <= r < h and 0 <= xoff+cc < w:
                        out[r][xoff+cc] = c
            yptr -= 1
    return out