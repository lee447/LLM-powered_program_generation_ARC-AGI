from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        if all(cell == 0 for cell in grid[i]):
            continue
        start = 0
        end = m
        for j in range(m):
            if grid[i][j] != 0:
                start = j
                break
        for j in range(m-1, -1, -1):
            if grid[i][j] != 0:
                end = j + 1
                break
        result.append(grid[i][start:end])
    return result