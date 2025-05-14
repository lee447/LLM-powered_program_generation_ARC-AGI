from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(0, len(grid), 3):
        for j in range(3):
            if i + j < len(grid):
                row = []
                for k in range(0, len(grid[0]), 3):
                    if k + 1 < len(grid[0]):
                        row.append(grid[i + j][k + 1])
                result.append(row)
    return result