def solve(grid):
    h = len(grid)
    w = len(grid[0])
    mid = w // 2
    border_rows = []
    for i, row in enumerate(grid):
        left = row[:mid]
        right = row[mid:]
        if all(x == left[0] for x in left) and all(x == 0 for x in right):
            border_rows.append(i)
    blocks = []
    for a, b in zip(border_rows, border_rows[1:]):
        if b - a > 1:
            blocks.append((a + 1, b - 1))
    colors = []
    for r0, r1 in blocks:
        col = None
        for i in range(r0, r1 + 1):
            for j in range(mid, w):
                if grid[i][j] != 0:
                    col = grid[i][j]
                    break
            if col is not None:
                break
        colors.append(col)
    if colors[0] > colors[-1]:
        new_colors = colors[::-1]
    else:
        new_colors = colors[1:] + colors[:1]
    out = [[None] * mid for _ in range(h)]
    for i in range(h):
        if i in border_rows:
            out[i] = grid[i][:mid]
        else:
            # find block index
            bi = 0
            for idx, (r0, r1) in enumerate(blocks):
                if r0 <= i <= r1:
                    bi = idx
                    break
            ccol = new_colors[bi]
            for j in range(mid):
                if grid[i][j] == 0:
                    out[i][j] = ccol
                else:
                    out[i][j] = grid[i][j]
    return out