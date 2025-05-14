from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        if all(cell == 0 for cell in grid[i]):
            break
        result.append(grid[i][m//3:m//3*2])
    return result