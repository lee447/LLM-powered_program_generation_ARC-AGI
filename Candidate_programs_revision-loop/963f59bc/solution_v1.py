def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    from copy import deepcopy
    result = [row[:] for row in grid]
    counts = {}
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v:
                counts[v] = counts.get(v, 0) + 1
    shape_color = next(c for c,ct in counts.items() if ct > 1)
    markers = [(r, c, grid[r][c]) for r in range(rows) for c in range(cols) if grid[r][c] not in (0, shape_color)]
    pts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == shape_color]
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxc = max(c for _, c in pts)
    H = maxr - minr + 1
    W = maxc - minc + 1
    mask = [[False]*W for _ in range(H)]
    for r, c in pts:
        mask[r-minr][c-minc] = True
    def hflip(m):
        return [row[::-1] for row in m]
    def vflip(m):
        return m[::-1]
    for mr, mc, mcol in markers:
        for orient in ('h','v'):
            if orient == 'h' and not (minr <= mr <= maxr): continue
            if orient == 'v' and not (minc <= mc <= maxc): continue
            mf = hflip(mask) if orient == 'h' else vflip(mask)
            fpts = [(i, j) for i in range(len(mf)) for j in range(len(mf[0])) if mf[i][j]]
            placed = False
            for i, j in fpts:
                tr = mr - i
                tc = mc - j
                ok = True
                for r0, c0 in fpts:
                    rr = tr + r0
                    cc = tc + c0
                    if not (0 <= rr < rows and 0 <= cc < cols):
                        ok = False
                        break
                    v = grid[rr][cc]
                    if v not in (0, mcol):
                        ok = False
                        break
                if ok:
                    for r0, c0 in fpts:
                        result[tr + r0][tc + c0] = mcol
                    placed = True
                    break
            if placed:
                break
    return result