from collections import deque, Counter

def solve(grid):
    H, W = len(grid), len(grid[0])
    cnt = Counter(v for row in grid for v in row)
    bg = cnt.most_common(1)[0][0]
    used = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != bg and not used[r][c]:
                q = deque([(r, c)])
                used[r][c] = True
                cells = []
                while q:
                    x, y = q.popleft()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not used[nx][ny] and grid[nx][ny] != bg:
                            used[nx][ny] = True
                            q.append((nx, ny))
                rs = [x for x,_ in cells]
                cs = [y for _,y in cells]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                cr = (minr + maxr)//2
                cc = (minc + maxc)//2
                offs = [(x-cr, y-cc) for x, y in cells]
                comps.append({"cells":cells, "center":(cr,cc), "offs":offs})
    singles = [c for c in comps if len(c["cells"])==1]
    iso = min(singles, key=lambda c: (c["center"][0], c["center"][1])) if singles else None
    tr, tc = iso["center"] if iso else (0,0)
    new = [[bg]*W for _ in range(H)]
    for comp in comps:
        cr, cc = comp["center"]
        offs = comp["offs"]
        if comp is iso:
            dr_shift = dc_shift = 0
        else:
            drs = any(dr!=0 for dr,dc in offs)
            dcs = any(dc!=0 for dr,dc in offs)
            if drs and dcs:
                dr_shift = 0
                dc_shift = tc - cc
            elif drs:
                dr_shift = 0
                dc_shift = 0
            elif dcs:
                dr_shift = tr - cr
                dc_shift = 0
            else:
                dr_shift = dc_shift = 0
        for dr, dc in offs:
            nr, nc = cr + dr + dr_shift, cc + dc + dc_shift
            if 0 <= nr < H and 0 <= nc < W:
                new[nr][nc] = grid[cr+dr][cc+dc]
    return new