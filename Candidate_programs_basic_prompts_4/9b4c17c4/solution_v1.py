def solve(grid):
    h, w = len(grid), len(grid[0])
    bgs = sorted({grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != 2})
    bg0, bg1 = bgs[0], bgs[1]
    reg_min = {bg0: w, bg1: w}
    reg_max = {bg0: -1, bg1: -1}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v in reg_min:
                reg_min[v] = min(reg_min[v], c)
                reg_max[v] = max(reg_max[v], c)
    res = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2 and not vis[i][j]:
                pts = []
                stack = [(i,j)]
                vis[i][j] = True
                while stack:
                    r,c = stack.pop()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 2 and not vis[rr][cc]:
                            vis[rr][cc] = True
                            stack.append((rr,cc))
                minr = min(r for r,c in pts)
                maxr = max(r for r,c in pts)
                minc = min(c for r,c in pts)
                maxc = max(c for r,c in pts)
                width = maxc - minc + 1
                b = None
                for r,c in pts:
                    for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                        rr,cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != 2:
                            b = grid[rr][cc]
                            break
                    if b is not None:
                        break
                if b == bg0:
                    new_min_c = reg_max[bg0] - width + 1
                else:
                    new_min_c = reg_min[bg1]
                for r,c in pts:
                    res[r][c] = b
                for r,c in pts:
                    newc = new_min_c + (c - minc)
                    res[r][newc] = 2
    return res