def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bands = []
    for i in range(h):
        if any(cell == 1 for cell in grid[i]):
            if not bands or i > bands[-1][1] + 1:
                bands.append([i, i])
            else:
                bands[-1][1] = i
    blocks = []
    for r0, r1 in bands:
        row = r0 + 1
        pts = []
        c = 0
        while c < w:
            if grid[row][c] == 1:
                c0 = c
                while c < w and grid[row][c] == 1:
                    c += 1
                pts.append((c0, c - 1))
            else:
                c += 1
        interiors = []
        for c0, c1 in pts:
            interiors.append(grid[row + 1][c0 + 1])
        blocks.append((pts, interiors))
    out = [list(r) for r in grid]
    for bi in range(len(bands) - 1):
        r0 = bands[bi][1] + 1
        r1 = bands[bi + 1][0] - 1
        if r0 > r1:
            continue
        height = r1 - r0 + 1
        pts0, val0 = blocks[bi]
        pts1, val1 = blocks[bi + 1]
        n0 = len(val0)
        n1 = len(val1)
        if height > 1:
            ps = [0, n0 - 1]
        else:
            ps = list(range(1, n0))
        for r in range(r0, r1 + 1):
            for p in ps:
                if p < n0:
                    c0, c1 = pts0[p]
                    if p == 0 or height == 1 or p < n1:
                        col = val0[p]
                    else:
                        col = val1[p] if p < n1 else val1[-1]
                    for c in range(c0 + 1, c1):
                        out[r][c] = col
    return out