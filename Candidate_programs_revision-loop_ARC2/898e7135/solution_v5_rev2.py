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
    seen = set()
    comps = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c!=0 and (i,j) not in seen:
                comp = bfs(i,j,c,seen)
                comps.append((c,comp))
    def is_border(comp):
        rs = [r for r,c in comp]; cs = [c for r,c in comp]
        r0,r1 = min(rs), max(rs); c0,c1 = min(cs), max(cs)
        per = 2*(r1-r0+1)+2*(c1-c0+1)-4
        return len(comp)==per
    border_col, bcomp = next((c,comp) for c,comp in comps if is_border(comp))
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
    others = sorted(others, key=lambda x:(min(r for r,c in x[1]), min(c for r,c in x[1])))
    margin = 2
    quad_h = (H - 2*margin)//2
    quad_w = (W - 2*margin)//2
    for idx, (c, comp) in enumerate(others):
        m = extract(comp)
        ph, pw = len(m), len(m[0])
        for _ in range(4):
            if ph<=quad_h and pw<=quad_w:
                break
            m = rotate_ccw(m)
            ph, pw = len(m), len(m[0])
        if idx==0:
            di, dj = 0, 0
        elif idx==1:
            di, dj = 0, quad_w-pw
        elif idx==2:
            di, dj = quad_h-ph, quad_w-pw
        else:
            di, dj = quad_h-ph, 0
        rm = [0,0,1,1][idx]
        cm = [0,1,1,0][idx]
        sr = margin + rm*quad_h + di
        sc = margin + cm*quad_w + dj
        for i in range(ph):
            for j in range(pw):
                if m[i][j]:
                    out[sr+i][sc+j] = c
    return out