def solve(grid):
    H, W = len(grid), len(grid[0])
    from math import isqrt
    # count global frequencies
    freq = {}
    for r in range(H):
        for c in range(W):
            freq[grid[r][c]] = freq.get(grid[r][c], 0) + 1
    # find monochrome block color whose count is a perfect square >=4
    block_color = None
    block_size = None
    for color, cnt in freq.items():
        k = isqrt(cnt)
        if k*k == cnt and k >= 2:
            # find bounding box of this color
            rs = [r for r in range(H) for c in range(W) if grid[r][c] == color]
            cs = [c for r in range(H) for c in range(W) if grid[r][c] == color]
            if rs and cs:
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                if (r1 - r0 + 1) * (c1 - c0 + 1) == cnt:
                    block_color = color
                    block_r0, block_c0 = r0, c0
                    block_h, block_w = r1 - r0 + 1, c1 - c0 + 1
                    break
    if block_color is None:
        return grid
    # find best mixed block of same size with a dominant color
    best = None
    best_score = -1
    for r in range(H - block_h + 1):
        for c in range(W - block_w + 1):
            if r == block_r0 and c == block_c0:
                continue
            # skip if it's the monochrome block
            vals = [grid[r+i][c+j] for i in range(block_h) for j in range(block_w)]
            s = set(vals)
            if len(s) <= 1:
                continue
            # score by max frequency
            mx = max(vals.count(x) for x in s)
            if mx > best_score:
                best_score = mx
                best = (r, c)
    if best is None:
        return grid
    sr, sc = best
    # copy
    out = [row[:] for row in grid]
    for i in range(block_h):
        for j in range(block_w):
            out[block_r0 + i][block_c0 + j] = grid[sr + i][sc + j]
    return out