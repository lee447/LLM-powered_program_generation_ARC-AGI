from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        if all(grid[r][c] == grid[r][0] for c in range(cols)):
            break
    return [row[1:cols-1] for row in grid[:r] if not all(x == row[0] for x in row)]