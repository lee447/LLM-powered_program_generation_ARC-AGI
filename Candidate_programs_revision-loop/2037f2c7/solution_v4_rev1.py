from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    def comps_of_color(v):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for i in range(h):
            for j in range(w):
                if grid[i][j]==v and not seen[i][j]:
                    q=deque([(i,j)])
                    seen[i][j]=True
                    comp=[]
                    while q:
                        r,c=q.popleft()
                        comp.append((r,c))
                        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            nr, nc = r+dr, c+dc
                            if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==v:
                                seen[nr][nc]=True
                                q.append((nr,nc))
                    comps.append(comp)
        return comps
    for v in range(1,10):
        cs = comps_of_color(v)
        if len(cs)==2:
            A, B = cs
            break
    r1s = [r for r,c in A]; c1s = [c for r,c in A]
    r2s = [r for r,c in B]; c2s = [c for r,c in B]
    r1min, c1min, r1max, c1max = min(r1s), min(c1s), max(r1s), max(c1s)
    r2min, c2min, r2max, c2max = min(r2s), min(c2s), max(r2s), max(c2s)
    h1, w1 = r1max-r1min+1, c1max-c1min+1
    h2, w2 = r2max-r2min+1, c2max-c2min+1
    h0, w0 = h1, w1
    arr1 = [[False]*w0 for _ in range(h0)]
    arr2 = [[False]*w0 for _ in range(h0)]
    for r,c in A: arr1[r-r1min][c-c1min] = True
    for r,c in B:
        rr, cc = r-r2min, c-c2min
        if 0<=rr<h0 and 0<=cc<w0: arr2[rr][cc] = True
    inter = [(r,c) for r in range(h0) for c in range(w0) if arr1[r][c] and arr2[r][w0-1-c]]
    rs = [r for r,c in inter]; cs = [c for r,c in inter]
    rmin, cmin, rmax, cmax = min(rs), min(cs), max(rs), max(cs)
    out = [[0]*(cmax-cmin+1) for _ in range(rmax-rmin+1)]
    for r,c in inter:
        out[r-rmin][c-cmin] = 8
    return out