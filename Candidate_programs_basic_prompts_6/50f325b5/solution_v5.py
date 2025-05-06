def solve(grid):
    R = len(grid)
    C = len(grid[0])
    coords = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == 8]
    if not coords:
        return grid
    minr = min(i for i, j in coords)
    maxr = max(i for i, j in coords)
    minc = min(j for i, j in coords)
    maxc = max(j for i, j in coords)
    shape = [(i - minr, j - minc) for i, j in coords]
    h, w = maxr - minr + 1, maxc - minc + 1
    variants = []
    hh, ww = h, w
    s = shape
    for _ in range(4):
        variants.append((s, hh, ww))
        s = [(c, hh - 1 - r) for r, c in s]
        hh, ww = ww, hh
    out = [row[:] for row in grid]
    for s, sh, sw in variants:
        for i in range(R - sh + 1):
            for j in range(C - sw + 1):
                ok = True
                for dr, dc in s:
                    if grid[i + dr][j + dc] != 3:
                        ok = False
                        break
                if ok:
                    for dr, dc in s:
                        out[i + dr][j + dc] = 8
    return out