from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(0, len(grid), 3):
        for j in range(3):
            if i + j < len(grid):
                row = grid[i + j]
                result.append([row[0], row[3], row[4], row[8], row[10]])
    return result