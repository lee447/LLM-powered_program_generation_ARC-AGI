def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = min(x for row in grid for x in row if row.count(x) == h * w)
    S = 5
    blocks = []
    for r in range(h - S + 1):
        for c in range(w - S + 1):
            b = grid[r][c]
            if b != bg:
                ok = True
                for i in range(S):
                    if grid[r][c + i] != b or grid[r + S - 1][c + i] != b or grid[r + i][c] != b or grid[r + i][c + S - 1] != b:
                        ok = False; break
                if not ok: continue
                f = grid[r + 1][c + 1]
                if f == b: continue
                for i in range(1, S - 1):
                    for j in range(1, S - 1):
                        if grid[r + i][c + j] != f:
                            ok = False; break
                    if not ok: break
                if ok:
                    blocks.append((r, c, b, f))
    blocks.sort(key=lambda x: (x[0] + x[1]))
    n = len(blocks)
    rows = int(n**0.5)
    if rows * rows < n: rows += 1
    cols = (n + rows - 1) // rows
    out = [[bg] * w for _ in range(h)]
    for idx, (r0, c0, bcol, fcol) in enumerate(blocks):
        rr = idx // cols
        cc = idx % cols
        nr = rr * (S + 1) + 1
        nc = cc * (S + 1) + 1
        for i in range(S):
            for j in range(S):
                if i in (0, S - 1) or j in (0, S - 1):
                    out[nr + i][nc + j] = bcol
                else:
                    out[nr + i][nc + j] = fcol
    return out