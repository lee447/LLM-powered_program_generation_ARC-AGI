from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    min_r, min_c = rows, cols
    max_r, max_c = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    result = []
    for r in range(min_r, min_r + 4):
        result.append(grid[r][min_c:min_c + 4])
    return result