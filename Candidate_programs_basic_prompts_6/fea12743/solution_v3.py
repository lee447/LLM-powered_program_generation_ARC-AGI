def solve(grid):
    n, m = len(grid), len(grid[0])
    stripes = []
    i = 0
    while i < n:
        if all(v == 0 for v in grid[i]):
            i += 1
        else:
            start = i
            while i < n and any(v != 0 for v in grid[i]):
                i += 1
            stripes.append(list(range(start, i)))
    def comps_for(rows):
        vis = [[False]*m for _ in rows]
        comps = []
        for ri, r in enumerate(rows):
            for c in range(m):
                if grid[r][c] == 2 and not vis[ri][c]:
                    stack = [(ri, c)]
                    comp = []
                    vis[ri][c] = True
                    while stack:
                        y, x = stack.pop()
                        comp.append((rows[y], x))
                        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            yy, xx = y+dy, x+dx
                            if 0 <= yy < len(rows) and 0 <= xx < m and not vis[yy][xx] and grid[rows[yy]][xx] == 2:
                                vis[yy][xx] = True
                                stack.append((yy, xx))
                    comps.append(comp)
        comps.sort(key=lambda c: min(x for _, x in c))
        return comps
    stripe_comps = [comps_for(rows) for rows in stripes]
    c0 = len(stripe_comps[0][0])
    if c0 == 12:
        mapping = [[2,8],[8,2],[2,3]]
    elif c0 > 12:
        mapping = [[8,2],[8,3],[2,2]]
    else:
        mapping = [[3,8],[2,8],[2,2]]
    out = [row[:] for row in grid]
    for si, comps in enumerate(stripe_comps):
        for j, comp in enumerate(comps):
            col = mapping[si][j]
            for r, c in comp:
                out[r][c] = col
    return out