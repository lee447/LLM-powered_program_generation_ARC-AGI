def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = grid
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if orig[i][j] == 1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and orig[nr][nc]==1:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(comp)
    for comp in comps:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                if r==minr or r==maxr or c==minc or c==maxc:
                    out[r][c] = 2
        ir0, ir1 = minr+1, maxr-1
        ic0, ic1 = minc+1, maxc-1
        if ir0<=ir1 and ic0<=ic1:
            rm = (ir0+ir1)//2
            cm = (ic0+ic1)//2
            for r in range(ir0, ir1+1):
                for c in range(ic0, ic1+1):
                    if orig[r][c] == 4:
                        if r<=rm and c<=cm:
                            out[r][c] = 8
                        else:
                            out[r][c] = 6
    return out