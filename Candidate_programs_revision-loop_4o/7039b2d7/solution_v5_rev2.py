from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    result = []
    for r in range(rows):
        if all(grid[r][c] == grid[r][0] for c in range(cols)):
            continue
        result.append([grid[r][c] for c in range(1, cols-1) if grid[r][c] != grid[r][0]])
    return result