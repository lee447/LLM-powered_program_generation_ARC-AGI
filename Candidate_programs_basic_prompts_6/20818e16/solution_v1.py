def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for r in grid:
        for c in r:
            counts[c] = counts.get(c, 0) + 1
    bg = max(counts, key=lambda k: counts[k])
    regions = []
    for color in sorted(counts):
        if color == bg: continue
        min_r, max_r = h, -1
        min_c, max_c = w, -1
        for i in range(h):
            for j in range(w):
                if grid[i][j] == color:
                    min_r = min(min_r, i)
                    max_r = max(max_r, i)
                    min_c = min(min_c, j)
                    max_c = max(max_c, j)
        regions.append((color, min_r, max_r, min_c, max_c))
    regions.sort(key=lambda x: (x[3]-x[2], x[4]-x[1]))
    blocks = []
    for color, r0, r1, c0, c1 in regions:
        sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
        bh = len(sub)
        if bh >= 2:
            blk = [sub[0], sub[-1]]
        else:
            blk = [sub[0], sub[0]]
        blocks.append((color, blk))
    out_h = 2 * len(blocks)
    max_w = max(len(b[1][0]) for b in blocks)
    out = []
    for color, blk in blocks:
        for row in blk:
            line = row + [row[-1]] * (max_w - len(row))
            out.append(line)
    return out