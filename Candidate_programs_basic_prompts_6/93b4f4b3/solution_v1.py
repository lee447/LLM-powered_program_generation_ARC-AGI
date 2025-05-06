def solve(grid):
    H, W = len(grid), len(grid[0])
    border = grid[0][0]
    lw = 0
    while lw < W and grid[0][lw] == border:
        lw += 1
    rw = W - lw
    right_start = lw
    frame_rows = [r for r in range(H) if all(grid[r][c] == border for c in range(lw))]
    hole_starts = [frame_rows[i] + 1 for i in range(len(frame_rows) - 1)]
    hole_height = frame_rows[1] - frame_rows[0] - 1
    shapes = []
    for start in hole_starts:
        cells = []
        for r in range(start, start + hole_height):
            for c in range(right_start + 1, right_start + rw - 1):
                v = grid[r][c]
                if v != 0:
                    cells.append((r - start, c - right_start - 1, v))
        shapes.append(cells)
    if hole_height % 2 == 0:
        shapes = shapes[1:] + shapes[:1]
    else:
        shapes = shapes[::-1]
    out = [row[:lw][:] for row in grid]
    for i, start in enumerate(hole_starts):
        for dr, dc, v in shapes[i]:
            out[start + dr][1 + dc] = v
    return out