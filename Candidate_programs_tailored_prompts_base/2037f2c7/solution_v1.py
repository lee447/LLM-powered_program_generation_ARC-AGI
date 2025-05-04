def solve(grid):
    H, W = len(grid), len(grid[0])
    nonz = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    if not nonz:
        return [[0]]
    r0 = min(r for r, c in nonz)
    r1 = max(r for r, c in nonz)
    c0 = min(c for r, c in nonz)
    c1 = max(c for r, c in nonz)
    block_h = None
    for r in range(r0, r1 + 1):
        if any(grid[r][c] != 0 for c in range(c0, c1 + 1)):
            if block_h is None:
                block_h = 1
            else:
                break
        elif block_h is not None:
            break
        if block_h is not None:
            block_h += 1
    total_h = r1 - r0 + 1
    m = total_h // block_h
    block_w = None
    for c in range(c0, c1 + 1):
        if any(grid[r][c] != 0 for r in range(r0, r1 + 1)):
            if block_w is None:
                block_w = 1
            else:
                break
        elif block_w is not None:
            break
        if block_w is not None:
            block_w += 1
    total_w = c1 - c0 + 1
    n = total_w // block_w
    out_h = m
    out_w = 2 * n + (block_w % 2)
    out = [[0]*out_w for _ in range(out_h)]
    for i in range(out_h):
        out[i][0] = 8
        out[i][-1] = 8
    for j in range(1, out_h-1):
        out[j][1] = 8
        out[j][-2] = 8
    return out