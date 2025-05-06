def solve(grid):
    rows, cols = len(grid), len(grid[0])
    grey = {r for r in range(rows) if all(cell == 5 for cell in grid[r])}
    shape_rows = [r for r in range(rows) if r not in grey and any(cell != 0 for cell in grid[r])]
    shape_rows.sort()
    starts = []
    lengths = []
    shapes = []
    for r in shape_rows:
        pos = [c for c in range(cols) if grid[r][c] != 0]
        if not pos: continue
        start, end = pos[0], pos[-1]
        starts.append(start)
        lengths.append(end - start + 1)
        shapes.append([grid[r][c] for c in range(start, end + 1)])
    n = len(starts)
    if n > 1:
        ds = (starts[-1] - starts[0]) // (n - 1)
        dl = (lengths[-1] - lengths[0]) // (n - 1)
    else:
        ds = dl = 0
    next_start = starts[-1] + ds
    next_len = lengths[-1] + dl
    base = shapes[0]
    if len(set(base)) == 1:
        fill = [base[0]] * next_len
    else:
        fill = base
    out = [[0] * cols for _ in range(3)]
    out[1][next_start:next_start + len(fill)] = fill
    return out