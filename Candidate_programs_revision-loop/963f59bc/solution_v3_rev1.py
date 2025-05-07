def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [row[:] for row in grid]
    counts = {}
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v:
                counts[v] = counts.get(v, 0) + 1
    shape_color = next(c for c, ct in counts.items() if ct > 1)
    pts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == shape_color]
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxc = max(c for _, c in pts)
    H = maxr - minr + 1
    W = maxc - minc + 1
    mask = [[False] * W for _ in range(H)]
    for r, c in pts:
        mask[r - minr][c - minc] = True
    def hflip(m):
        return [row[::-1] for row in m]
    def vflip(m):
        return m[::-1]
    for mr in range(rows):
        for mc in range(cols):
            mcol = grid[mr][mc]
            if mcol and mcol != shape_color:
                if minr <= mr <= maxr:
                    mf = hflip(mask)
                    rel_r = mr - minr
                    for j in range(W):
                        if mf[rel_r][j]:
                            break
                    tr = minr
                    tc = mc - j
                else:
                    mf = vflip(mask)
                    rel_c = mc - minc
                    for i in range(H):
                        if mf[i][rel_c]:
                            break
                    tr = mr - i
                    tc = minc
                for i in range(H):
                    for j in range(W):
                        if mf[i][j]:
                            result[tr + i][tc + j] = mcol
    return result