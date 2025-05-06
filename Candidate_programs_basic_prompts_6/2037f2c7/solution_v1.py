from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                cells = [(i,j)]
                seen[i][j] = True
                q = [(i,j)]
                bi, bj, ei, ej = i, j, i, j
                while q:
                    y,x = q.pop()
                    for dy,dx in dirs:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != 0 and not seen[ny][nx]:
                            seen[ny][nx] = True
                            q.append((ny,nx))
                            cells.append((ny,nx))
                            bi, bj = min(bi,ny), min(bj,nx)
                            ei, ej = max(ei,ny), max(ej,nx)
                comps.append((cells, bi, bj, ei, ej))
    # choose component
    best = None
    for comp in comps:
        cells, bi, bj, ei, ej = comp
        sub = [row[bj:ej+1] for row in grid[bi:ei+1]]
        vs = {}
        for row in sub:
            for v in row:
                if v!=0: vs[v]=vs.get(v,0)+1
        if not vs: continue
        # prefer comp containing 6, else 7, else largest
        contains6 = any(grid[i][j]==6 for i,j in cells)
        contains7 = any(grid[i][j]==7 for i,j in cells)
        size = (ei-bi+1)*(ej-bj+1)
        score = (contains6*1000 + contains7*100 + size)
        if best is None or score>best[0]:
            best = (score, comp)
    _, (cells, bi, bj, ei, ej) = best
    sub = [row[bj:ej+1] for row in grid[bi:ei+1]]
    hh, ww = len(sub), len(sub[0])
    # find central color
    freq = {}
    for row in sub:
        for v in row:
            if v!=0: freq[v]=freq.get(v,0)+1
    if not freq:
        return []
    central = max(freq, key=lambda k: freq[k])
    # find edge color (second most frequent)
    cand = [(cnt,v) for v,cnt in freq.items() if v!=central]
    if not cand:
        edge = central
    else:
        edge = max(cand)[1]
    # build mask of edge color
    mask = [[1 if sub[i][j]==edge else 0 for j in range(ww)] for i in range(hh)]
    # count per row
    rows = []
    for i in range(hh):
        s = sum(mask[i])
        if s>0:
            rows.append((s,i))
    if not rows:
        return []
    # find B and A
    rs = [s for s,_ in rows]
    mn = min(rs)
    mx = max(rs)
    # first B
    b0 = next(i for s,i in rows if s==mn)
    # first A
    a0 = next(i for s,i in rows if s==mx)
    # choose output rows
    if hh%2==0:
        picks = [b0,a0,b0,a0]
    else:
        picks = [b0,a0,b0]
    out = []
    for r in picks:
        out.append([8 if mask[r][c] else 0 for c in range(ww)])
    return out