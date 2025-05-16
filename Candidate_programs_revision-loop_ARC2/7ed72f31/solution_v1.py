def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    mid_r, mid_c = (h - 1) / 2, (w - 1) / 2
    res = [row[:] for row in grid]
    vis = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not vis[i][j]:
                color = grid[i][j]
                stack = [(i, j)]
                comp = []
                vis[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == color:
                            vis[nr][nc] = True
                            stack.append((nr, nc))
                if color == bg or color == 2:
                    continue
                rs = [r for r, _ in comp]
                cs = [c for _, c in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                bh = r1 - r0 + 1
                bw = c1 - c0 + 1
                cen_r = (r0 + r1) / 2
                cen_c = (c0 + c1) / 2
                if bh == bw:
                    dr = -1 if cen_r > mid_r else 1
                    dc = -1 if cen_c > mid_c else 1
                    rr = dr * (bh + 1)
                    cc = dc * bw
                elif bh > bw:
                    dr = 0
                    dc = 1 if cen_c > mid_c else -1
                    rr = 0
                    cc = dc * (bw + 1)
                else:
                    dr = 1 if cen_r > mid_r else -1
                    dc = 0
                    rr = dr * (bh + 1)
                    cc = 0
                for r, c in comp:
                    nr, nc = r + rr, c + cc
                    if 0 <= nr < h and 0 <= nc < w:
                        res[nr][nc] = color
    return res