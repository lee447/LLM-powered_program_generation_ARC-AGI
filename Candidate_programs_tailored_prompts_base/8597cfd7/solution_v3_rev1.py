from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    split = next(i for i, row in enumerate(grid) if all(cell == 5 for cell in row))
    colors = {v for row in grid for v in row if v not in (0, 5)}
    col_of = {}
    for c in range(w):
        for r in range(h):
            v = grid[r][c]
            if v in colors:
                col_of[v] = c
                break
    best_c = None
    best_diff = -1
    for c in colors:
        col = col_of[c]
        curr = 0
        max_above = 0
        for r in range(split):
            if grid[r][col] == c:
                curr += 1
                if curr > max_above:
                    max_above = curr
            else:
                curr = 0
        curr = 0
        max_below = 0
        for r in range(split + 1, h):
            if grid[r][col] == c:
                curr += 1
                if curr > max_below:
                    max_below = curr
            else:
                curr = 0
        diff = abs(max_above - max_below)
        if diff > best_diff or (diff == best_diff and (best_c is None or c < best_c)):
            best_diff = diff
            best_c = c
    return [[best_c, best_c], [best_c, best_c]]