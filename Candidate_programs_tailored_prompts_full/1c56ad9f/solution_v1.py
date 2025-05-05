def solve(grid):
    H, W = len(grid), len(grid[0])
    cells = [(r, c, grid[r][c]) for r in range(H) for c in range(W) if grid[r][c] != 0]
    by_row = {}
    for r, c, v in cells:
        by_row.setdefault(r, []).append((c, v))
    spans = {r: max(cs := [c for c, _ in by_row[r]]) - min(cs) + 1 for r in by_row}
    maxspan = max(spans.values())
    bar_rows = sorted(r for r, sp in spans.items() if sp == maxspan)
    if not bar_rows:
        return grid
    top, bottom = bar_rows[0], bar_rows[-1]
    interior = [r for r in sorted(by_row) if top < r < bottom]
    result = [[0]*W for _ in range(H)]
    for r, c, v in cells:
        result[r][c] = 0
    j = 0
    shifts = {}
    for r in interior:
        j += 1
        shifts[r] = -1 if j % 2 == 1 else 1
    for r, c, v in cells:
        d = shifts.get(r, 0)
        result[r][c + d] = v
    return result