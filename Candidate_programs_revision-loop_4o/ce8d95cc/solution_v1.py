from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(0, len(grid), 3):
        row = []
        for j in range(0, len(grid[0]), 3):
            row.append(grid[i][j+1])
            if j+4 < len(grid[0]):
                row.append(grid[i][j+4])
        result.append(row)
    return result