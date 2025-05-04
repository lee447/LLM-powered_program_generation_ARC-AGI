def solve(grid):
    h, w = len(grid), len(grid[0])
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    r1 = min(r for r, c in ones)
    legend_row = r1 - 1
    origins = [(grid[legend_row][c], legend_row, c) for c in range(w) if grid[legend_row][c] != 0]
    shapes = {}
    for color, ro, co in origins:
        shapes[color] = []
    for r, c in ones:
        best = min(origins, key=lambda oc: abs(r - oc[1]) + abs(c - oc[2]))
        color, ro, co = best
        shapes[color].append((r - ro, c - co))
    norms = {}
    for color, pts in shapes.items():
        drs = [dr for dr, dc in pts]
        dcs = [dc for dr, dc in pts]
        dr0, dc0 = min(drs), min(dcs)
        norms[color] = [(dr - dr0, dc - dc0) for dr, dc in pts]
    all_norms = list(norms.values())
    blockh = max(dr for pts in all_norms for dr, dc in pts) + 1
    blockw = max(dc for pts in all_norms for dr, dc in pts) + 1
    drs, dcs = blockh + 1, blockw + 1
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    minr = min(r for r, c in fives)
    maxr = max(r for r, c in fives)
    minc = min(c for r, c in fives)
    maxc = max(c for r, c in fives)
    H, W = maxr - minr + 1, maxc - minc + 1
    out = [[0] * W for _ in range(H)]
    for r in range(minr, maxr + 1):
        for c in range(minc, maxc + 1):
            v = grid[r][c]
            if v != 0 and v != 5:
                br = (r - minr) // drs
                bc = (c - minc) // dcs
                r0 = minr + br * drs
                c0 = minc + bc * dcs
                for dr, dc in norms[v]:
                    orr = r0 - minr + dr
                    occ = c0 - minc + dc
                    out[orr][occ] = v
    return out