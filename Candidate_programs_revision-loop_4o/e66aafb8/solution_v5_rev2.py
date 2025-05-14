from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        if all(cell == 0 for cell in grid[i]):
            continue
        result.append(grid[i][m//3:m//3*2])
    return [row for row in result if any(cell != 0 for cell in row)]