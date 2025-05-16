def solve(grid):
    R, C = len(grid), len(grid[0])
    r0, r1, c0, c1 = R, -1, C, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 8:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    mask_h, mask_w = r1 - r0 + 1, c1 - c0 + 1
    good_cols = [j for j in range(C) if all(grid[i][j] != 8 for i in range(R))]
    tile_h = mask_h
    for p in range(2, R):
        ok = True
        for j in good_cols:
            for i in range(R - p):
                if grid[i][j] != grid[i + p][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            tile_h = p
            break
    good_rows = [i for i in range(R) if all(grid[i][j] != 8 for j in range(C))]
    tile_w = mask_w
    for q in range(2, C):
        ok = True
        for i in good_rows:
            for j in range(C - q):
                if grid[i][j] != grid[i][j + q]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            tile_w = q
            break
    sr0 = r0 - (r0 % tile_h)
    sc0 = c0 - (c0 % tile_w)
    for k in range((R - sr0) // tile_h + 1):
        for l in range((C - sc0) // tile_w + 1):
            sr = sr0 + k * tile_h
            sc = sc0 + l * tile_w
            if sr + tile_h <= R and sc + tile_w <= C:
                block = [row[sc:sc + tile_w] for row in grid[sr:sr + tile_h]]
                if all(block[i][j] != 8 for i in range(tile_h) for j in range(tile_w)) and not (sr == sr0 and sc == sc0):
                    return block
    return []