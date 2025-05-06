def solve(grid):
    H = len(grid)
    W = len(grid[0])
    left_w = next(j for j in range(W) if all(grid[r][j] == 0 for r in range(H)))
    mask = [[grid[r][c] == 0 for c in range(left_w)] for r in range(H)]
    blocks = []
    in_block = False
    for r in range(H):
        if any(mask[r]):
            if not in_block:
                start = r
                in_block = True
        else:
            if in_block:
                blocks.append((start, r))
                in_block = False
    if in_block:
        blocks.append((start, H))
    shapes = []
    for s, e in blocks:
        m = []
        color = None
        for r in range(s, e):
            for c in range(left_w):
                if mask[r][c]:
                    v = grid[r][left_w + c]
                    if v != 0:
                        m.append((r, c))
                        color = v
        shapes.append((m, color))
    n = len(shapes)
    out = [row[:left_w] for row in grid]
    for i, (m, _) in enumerate(shapes):
        m2, color2 = shapes[(i + 1) % n]
    for i, (m2, color2) in enumerate([shapes[(i + 1) % n] for i in range(n)]):
        for r, c in m2:
            out[r][c] = color2
    return out