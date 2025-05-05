from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    cells = [(r, c, grid[r][c]) for r in range(H) for c in range(W) if grid[r][c] != 0]
    by_row = {}
    for r, c, v in cells:
        by_row.setdefault(r, []).append(c)
    spans = {r: max(cs) - min(cs) + 1 for r, cs in by_row.items()}
    maxspan = max(spans.values())
    bar_rows = sorted(r for r, sp in spans.items() if sp == maxspan)
    top, bottom = bar_rows[0], bar_rows[-1]
    arr = [0, -1, 0, 1]
    result = [[0]*W for _ in range(H)]
    for r, c, v in cells:
        if top <= r <= bottom:
            shift = arr[(r - top) % 4]
        else:
            shift = 0
        result[r][c+shift] = v
    return result