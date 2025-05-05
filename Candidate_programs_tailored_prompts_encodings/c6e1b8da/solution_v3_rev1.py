from collections import deque, defaultdict

def solve(grid):
    h, w = len(grid), len(grid[0])
    empty_rows = []
    i = 0
    while i < h:
        if all(grid[i][j] == 0 for j in range(w)):
            j = i
            while j < h and all(grid[j][k] == 0 for k in range(w)):
                j += 1
            empty_rows.append((i, j - 1))
            i = j
        else:
            i += 1
    midr = h / 2
    empty_rows_center = [(a, b) for a, b in empty_rows if a > 0 and b < h - 1]
    rs = empty_rows_center if empty_rows_center else empty_rows
    cr0, cr1 = min(rs, key=lambda x: abs((x[0] + x[1]) / 2 - midr))
    empty_cols = []
    j = 0
    while j < w:
        if all(grid[i][j] == 0 for i in range(h)):
            k = j
            while k < w and all(grid[i][k] == 0 for i in range(h)):
                k += 1
            empty_cols.append((j, k - 1))
            j = k
        else:
            j += 1
    midc = w / 2
    empty_cols_center = [(a, b) for a, b in empty_cols if a > 0 and b < w - 1]
    cs = empty_cols_center if empty_cols_center else empty_cols
    if cs:
        cc0, cc1 = min(cs, key=lambda x: abs((x[0] + x[1]) / 2 - midc))
    else:
        cc0, cc1 = w // 2 - 1, w // 2
    qr = [(0, cr0 - 1, 0, cc0 - 1), (0, cr0 - 1, cc1 + 1, w - 1),
          (cr1 + 1, h - 1, cc1 + 1, w - 1), (cr1 + 1, h - 1, 0, cc0 - 1)]
    vis = [[False] * w for _ in range(h)]
    comps = defaultdict(list)
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                col = grid[i][j]
                q = deque([(i, j)])
                pts = []
                vis[i][j] = True
                while q:
                    x, y = q.popleft()
                    pts.append((x, y))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == col:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                rs_ = [p[0] for p in pts]; cs_ = [p[1] for p in pts]
                r0, r1, c0, c1 = min(rs_), max(rs_), min(cs_), max(cs_)
                mask = [[0] * (c1 - c0 + 1) for _ in range(r1 - r0 + 1)]
                for x, y in pts:
                    mask[x - r0][y - c0] = col
                for qi, (tr0, tr1, tc0, tc1) in enumerate(qr):
                    if r0 >= tr0 and r1 <= tr1 and c0 >= tc0 and c1 <= tc1:
                        comps[qi].append((r0, r1, c0, c1, mask))
                        break
    newcomps = defaultdict(list)
    for qi, clist in comps.items():
        for comp in clist:
            newcomps[(qi + 1) % 4].append(comp)
    out = [row[:] for row in grid]
    for clist in comps.values():
        for r0, r1, c0, c1, _ in clist:
            for x in range(r0, r1 + 1):
                for y in range(c0, c1 + 1):
                    out[x][y] = 0
    for qi, clist in newcomps.items():
        for r0, r1, c0, c1, mask in clist:
            h0, w0 = r1 - r0 + 1, c1 - c0 + 1
            if qi == 0:
                nr1 = cr0 - 1; nr0 = nr1 - h0 + 1
                nc1 = cc0 - 1; nc0 = nc1 - w0 + 1
            elif qi == 1:
                nr1 = cr0 - 1; nr0 = nr1 - h0 + 1
                nc0 = cc1 + 1; nc1 = nc0 + w0 - 1
            elif qi == 2:
                nr0 = cr1 + 1; nr1 = nr0 + h0 - 1
                nc0 = cc1 + 1; nc1 = nc0 + w0 - 1
            else:
                nr0 = cr1 + 1; nr1 = nr0 + h0 - 1
                nc1 = cc0 - 1; nc0 = nc1 - w0 + 1
            for i0 in range(h0):
                for j0 in range(w0):
                    v = mask[i0][j0]
                    if v:
                        out[nr0 + i0][nc0 + j0] = v
    return out