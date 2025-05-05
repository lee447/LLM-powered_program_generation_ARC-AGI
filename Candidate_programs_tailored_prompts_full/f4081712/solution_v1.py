def solve(grid):
    nrows, ncols = len(grid), len(grid[0])
    def neighbors(r,c):
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr,cc = r+dr, c+dc
            if 0 <= rr < nrows and 0 <= cc < ncols:
                yield rr,cc
    stripe_color = None
    stripe_comps = None
    for c in (3,4):
        seen = [[False]*ncols for _ in range(nrows)]
        comps = []
        for r in range(nrows):
            for co in range(ncols):
                if grid[r][co] == c and not seen[r][co]:
                    stack = [(r,co)]
                    comp = []
                    seen[r][co] = True
                    while stack:
                        x,y = stack.pop()
                        comp.append((x,y))
                        for nx,ny in neighbors(x,y):
                            if grid[nx][ny] == c and not seen[nx][ny]:
                                seen[nx][ny] = True
                                stack.append((nx,ny))
                    comps.append(comp)
        hor, ver = [], []
        for comp in comps:
            rs = [p[0] for p in comp]
            cs = [p[1] for p in comp]
            h = max(rs)-min(rs)+1
            w = max(cs)-min(cs)+1
            if w > h and len(comp) > ncols//2:
                hor.append(comp)
            if h > w and len(comp) > nrows//2:
                ver.append(comp)
        if hor and ver:
            stripe_color = c
            stripe_comps = (hor, ver)
            break
    hor, ver = stripe_comps
    center_r, center_c = nrows/2, ncols/2
    def pick_line(comps, center, axis):
        best = None
        bd = 1e9
        for comp in comps:
            coords = [p[axis] for p in comp]
            m = (min(coords)+max(coords))/2
            d = abs(m-center)
            if d < bd:
                bd = d
                best = comp
        return best
    comp_h = pick_line(hor, center_r, 0)
    comp_v = pick_line(ver, center_c, 1)
    rs = [p[0] for p in comp_h]
    row_h = (min(rs) + max(rs))//2
    cs = [p[1] for p in comp_v]
    col_v = (min(cs) + max(cs))//2
    for dr in (1,-1):
        for dc in (1,-1):
            sr, sc = row_h+dr, col_v+dc
            if not (0 <= sr < nrows and 0 <= sc < ncols): continue
            v = grid[sr][sc]
            if v == 0: continue
            seen2 = [[False]*ncols for _ in range(nrows)]
            stack = [(sr,sc)]
            seen2[sr][sc] = True
            minr, maxr, minc, maxc = sr, sr, sc, sc
            while stack:
                x,y = stack.pop()
                minr, maxr = min(minr,x), max(maxr,x)
                minc, maxc = min(minc,y), max(maxc,y)
                for nx,ny in neighbors(x,y):
                    if grid[nx][ny] == v and not seen2[nx][ny]:
                        seen2[nx][ny] = True
                        stack.append((nx,ny))
            ok = True
            for r in range(minr, maxr+1):
                for c in range(minc, maxc+1):
                    if grid[r][c] != v:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            return [row[minc:maxc+1] for row in grid[minr:maxr+1]]
    return []
# Example usage:
# result = solve(input_grid)