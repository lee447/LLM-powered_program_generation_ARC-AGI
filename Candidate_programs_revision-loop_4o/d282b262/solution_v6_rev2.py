from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        non_zero_elements = [grid[i][j] for j in range(m) if grid[i][j] != 0]
        if non_zero_elements:
            result[i][-len(non_zero_elements):] = non_zero_elements
    return result