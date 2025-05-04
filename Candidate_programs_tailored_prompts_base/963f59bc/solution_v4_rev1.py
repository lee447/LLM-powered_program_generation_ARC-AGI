from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    ones = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == 1]
    colors = [(x, y) for y in range(h) for x in range(w) if grid[y][x] not in (0, 1)]
    cy_list = [y for _, y in colors]
    cy0 = cy_list[0]
    row_counts = {}
    for x, y in ones:
        row_counts[y] = row_counts.get(y, 0) + 1
    candidates = [r for r, cnt in row_counts.items() if cnt == 1]
    anchor_row = min(candidates, key=lambda r: abs(r - cy0))
    anchor_col = next(x for x, y in ones if y == anchor_row)
    offsets = [(x - anchor_col, y - anchor_row) for x, y in ones]
    out = [row[:] for row in grid]
    for cx, cy in colors:
        c = grid[cy][cx]
        for dx, dy in offsets:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and out[ny][nx] != 1:
                out[ny][nx] = c
    return out