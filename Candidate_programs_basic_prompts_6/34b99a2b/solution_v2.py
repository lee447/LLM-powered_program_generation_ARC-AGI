from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    delim = next(c for c in range(cols) if all(grid[r][c] == 4 for r in range(rows)))
    w = delim
    return [[int((grid[r][i] != 0) != (grid[r][delim + 1 + i] != 0)) * 2 for i in range(w)] for r in range(rows)]