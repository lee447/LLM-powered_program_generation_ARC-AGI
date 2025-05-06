def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    def comps_of_color(v):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for i in range(h):
            for j in range(w):
                if grid[i][j]==v and not seen[i][j]:
                    q = deque([(i,j)])
                    seen[i][j] = True
                    comp = []
                    while q:
                        r,c = q.popleft()
                        comp.append((r,c))
                        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            nr, nc = r+dr, c+dc
                            if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==v:
                                seen[nr][nc] = True
                                q.append((nr,nc))
                    comps.append(comp)
        return comps
    # find color with exactly 2 components
    for v in range(9,0,-1):
        comps = comps_of_color(v)
        if len(comps)==2:
            A, B = comps
            break
    def normalize(comp):
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        r0, c0 = min(rs), min(cs)
        return {(r-r0, c-c0) for r,c in comp}
    Arel = normalize(A)
    Brel = normalize(B)
    inter = Arel & Brel
    if not inter:
        inter = Arel | Brel
    rs = [r for r,c in inter]
    cs = [c for r,c in inter]
    rmin, cmin = min(rs), min(cs)
    rmax, cmax = max(rs), max(cs)
    out = [[0]*(cmax-cmin+1) for _ in range(rmax-rmin+1)]
    for r,c in inter:
        out[r-rmin][c-cmin] = 8
    return out