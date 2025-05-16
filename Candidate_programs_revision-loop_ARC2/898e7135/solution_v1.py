from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(sr, sc, color, seen):
        q = [(sr,sc)]
        comp = [(sr,sc)]
        seen.add((sr,sc))
        for r,c in q:
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<h and 0<=nc<w and (nr,nc) not in seen and grid[nr][nc]==color:
                    seen.add((nr,nc))
                    q.append((nr,nc))
                    comp.append((nr,nc))
        return comp
    comps = []
    seen = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and (i,j) not in seen:
                comp = bfs(i,j, grid[i][j], seen)
                comps.append((grid[i][j], comp))
    def is_border(color, comp):
        rs = [r for r,c in comp]; cs = [c for r,c in comp]
        r0,r1 = min(rs), max(rs); c0,c1 = min(cs), max(cs)
        per = 2*(r1-r0+1)+2*(c1-c0+1)-4
        return len(comp)==per
    border_col = next(c for c,comp in comps if is_border(c,comp))
    bcomp = next(comp for c,comp in comps if c==border_col and is_border(c,comp))
    rs = [r for r,c in bcomp]; cs = [c for r,c in bcomp]
    r0,r1 = min(rs), max(rs); c0,c1 = min(cs), max(cs)
    hi, wi = r1-r0+1, c1-c0+1
    H, W = 2*hi, 2*wi
    out = [[border_col]*W for _ in range(H)]
    others = [(c,comp) for c,comp in comps if c!=border_col and len(comp)>1]
    def extract(comp):
        rs = [r for r,c in comp]; cs = [c for r,c in comp]
        r0,r1 = min(rs), max(rs); c0,c1 = min(cs), max(cs)
        h0, w0 = r1-r0+1, c1-c0+1
        m = [[0]*w0 for _ in range(h0)]
        for r,c in comp:
            m[r-r0][c-c0] = 1
        return m
    def rotate_ccw(m):
        h0, w0 = len(m), len(m[0])
        r = [[0]*h0 for _ in range(w0)]
        for i in range(w0):
            for j in range(h0):
                r[i][j] = m[j][w0-1-i]
        return r
    placed = []
    for c, comp in others:
        m = extract(comp)
        for _ in range(4):
            if len(m)<=H//2 and len(m[0])<=W//2:
                break
            m = rotate_ccw(m)
        placed.append((c,m))
    placed.sort(key=lambda x: -sum(sum(row) for row in x[1]))
    pos = [ (1,1), (1, W-1), (H-1, W-1), (H-1,1) ]
    for idx, (c,m) in enumerate(placed):
        if idx>=3: break
        ph, pw = len(m), len(m[0])
        r0,c0 = pos[idx]
        if c0>1: c0 -= pw
        if r0>1: r0 -= ph
        for i in range(ph):
            for j in range(pw):
                if m[i][j]:
                    out[r0+i][c0+j] = c
    return out