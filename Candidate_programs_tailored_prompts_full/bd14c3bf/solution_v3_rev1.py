import collections

def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def cc_cells(val):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for i in range(h):
            for j in range(w):
                if grid[i][j]==val and not seen[i][j]:
                    q=[(i,j)]; seen[i][j]=True; comp=[]
                    while q:
                        r,c=q.pop()
                        comp.append((r,c))
                        for dr,dc in dirs:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==val:
                                seen[nr][nc]=True; q.append((nr,nc))
                    comps.append(comp)
        return comps

    # find the one "pattern" cluster of 1s
    ones = cc_cells(1)
    if not ones:
        return grid
    pat = max(ones, key=len)
    r0 = min(r for r,c in pat)
    c0 = min(c for r,c in pat)
    pr = max(r for r,c in pat)-r0+1
    pc = max(c for r,c in pat)-c0+1
    patset = set((r-r0,c-c0) for r,c in pat)

    # find red components
    reds = cc_cells(2)
    for comp in reds:
        rmin = min(r for r,c in comp)
        rmax = max(r for r,c in comp)
        cmin = min(c for r,c in comp)
        cmax = max(c for r,c in comp)
        H = rmax-rmin+1
        W = cmax-cmin+1
        # skip the one that already holds the pattern
        inside = [(r,c) for r in range(rmin,rmax+1) for c in range(cmin,cmax+1)]
        if any(grid[r][c]==1 for r,c in inside):
            continue
        # enough room?
        if H==pr and W==pc:
            for dr,dc in patset:
                grid[rmin+dr][cmin+dc] = 1
        elif H==pc and W==pr:
            # transpose
            for dr,dc in patset:
                grid[rmin+dc][cmin+dr] = 1
    return grid